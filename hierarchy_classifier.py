# hierarchy_classifier.py
from sentence_transformers import SentenceTransformer, util
from iso_categories import ISO_CATEGORIES

def get_category_nodes(tree, parent_path=[]):
    nodes = []
    for cat, info in tree.items():
        current_path = parent_path + [cat]
        nodes.append({
            'path': current_path,
            'description': info['description'],
            'subcategories': info['subcategories']
        })
        if info['subcategories']:
            nodes.extend(get_category_nodes(info['subcategories'], current_path))
    return nodes

def load_model():
    # Load a small efficient model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model

def build_index(model):
    all_nodes = get_category_nodes(ISO_CATEGORIES)
    nodes_by_level = {}
    for n in all_nodes:
        level = len(n['path'])
        if level not in nodes_by_level:
            nodes_by_level[level] = []
        n['embedding'] = model.encode(n['description'], convert_to_tensor=True)
        nodes_by_level[level].append(n)
    return nodes_by_level

def find_best_match(embedding, candidates):
    best_score = -1
    best_node = None
    for c in candidates:
        score = float(util.pytorch_cos_sim(embedding, c['embedding']))
        if score > best_score:
            best_score = score
            best_node = c
    return best_node, best_score

def classify_field_of_work(text, model, nodes_by_level, max_depth=4):
    # Actual text should be preprocessed and translated before calling this
    if not text or text.strip().lower() in ['n/a', 'na', 'none', '-']:
        return None

    text_embedding = model.encode(text, convert_to_tensor=True)
    path = []
    current_level = 1
    
    while current_level <= max_depth and current_level in nodes_by_level:
        candidates = [n for n in nodes_by_level[current_level]
                      if n['path'][:current_level-1] == path[:current_level-1]]
        if not candidates:
            break
        
        best_node, score = find_best_match(text_embedding, candidates)
        path = best_node['path']
        
        # If more subcategories exist and not at max depth, go deeper
        if best_node['subcategories'] and current_level < max_depth:
            current_level += 1
        else:
            break
    return path if path else None
