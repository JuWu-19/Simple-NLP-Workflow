# iso_categories.py
# This file defines the ISO-like hierarchical category structure as a Python dictionary.

ISO_CATEGORIES = {
    "Healthcare": {
        "description": "Healthcare and medical services",
        "subcategories": {
            "Pharmaceuticals": {
                "description": "Pharmaceutical industry, drug discovery, biotech",
                "subcategories": {
                    "R&D": {
                        "description": "Pharmaceutical research and development",
                        "subcategories": {
                            "Clinical Trials": {
                                "description": "Design and conduct of clinical trials",
                                "subcategories": {}
                            },
                            "Drug Discovery": {
                                "description": "Identification and optimization of new drug candidates",
                                "subcategories": {}
                            },
                            "Regulatory Affairs": {
                                "description": "Ensuring compliance with medical regulations",
                                "subcategories": {}
                            }
                        }
                    },
                    "Manufacturing": {
                        "description": "Drug manufacturing and production",
                        "subcategories": {
                            "Active Pharmaceutical Ingredients (API)": {
                                "description": "Production of key chemical components",
                                "subcategories": {}
                            },
                            "Formulation": {
                                "description": "Combining APIs with excipients to create final dosage forms",
                                "subcategories": {}
                            },
                            "Quality Control": {
                                "description": "Testing products to ensure standards are met",
                                "subcategories": {}
                            }
                        }
                    },
                    "Distribution": {
                        "description": "Supply chain and logistics of pharmaceutical products",
                        "subcategories": {
                            "Wholesale": {
                                "description": "Bulk distribution of drugs to pharmacies and hospitals",
                                "subcategories": {}
                            },
                            "Retail Pharmacy": {
                                "description": "Community or online pharmacies selling to end consumers",
                                "subcategories": {}
                            },
                            "Cold Chain Logistics": {
                                "description": "Managing temperature-sensitive products",
                                "subcategories": {}
                            }
                        }
                    }
                }
            },
            "Healthcare Services": {
                "description": "Hospitals, clinics, patient care",
                "subcategories": {
                    "Hospitals": {
                        "description": "Inpatient facilities providing comprehensive care",
                        "subcategories": {
                            "Public Hospitals": {
                                "description": "Government-funded hospitals",
                                "subcategories": {}
                            },
                            "Private Hospitals": {
                                "description": "Privately owned hospitals",
                                "subcategories": {}
                            },
                            "Specialized Centers": {
                                "description": "Focus on specific areas like oncology, cardiology",
                                "subcategories": {}
                            }
                        }
                    },
                    "Clinics": {
                        "description": "Outpatient healthcare facilities",
                        "subcategories": {
                            "Primary Care Clinics": {
                                "description": "First point of contact for general health issues",
                                "subcategories": {}
                            },
                            "Dental Clinics": {
                                "description": "Specialized in oral health services",
                                "subcategories": {}
                            },
                            "Urgent Care Centers": {
                                "description": "Walk-in clinics for immediate but non-emergency care",
                                "subcategories": {}
                            }
                        }
                    },
                    "Telemedicine": {
                        "description": "Remote delivery of healthcare services",
                        "subcategories": {
                            "Tele-Consultations": {
                                "description": "Video or phone consultations",
                                "subcategories": {}
                            },
                            "Tele-Radiology": {
                                "description": "Remote analysis of medical images",
                                "subcategories": {}
                            },
                            "Remote Patient Monitoring": {
                                "description": "Monitoring patients remotely using devices and sensors",
                                "subcategories": {}
                            }
                        }
                    }
                }
            },
            "Medical Devices": {
                "description": "Equipment and tools used in healthcare",
                "subcategories": {
                    "Diagnostic Devices": {
                        "description": "Equipment to diagnose conditions",
                        "subcategories": {
                            "Imaging Machines (MRI, CT)": {
                                "description": "Medical imaging equipment",
                                "subcategories": {}
                            },
                            "Point-of-Care Testing Kits": {
                                "description": "Tests performed at the time and place of patient care",
                                "subcategories": {}
                            },
                            "In Vitro Diagnostics": {
                                "description": "Tests on samples outside the organism",
                                "subcategories": {}
                            }
                        }
                    },
                    "Surgical Instruments": {
                        "description": "Tools used in surgical procedures",
                        "subcategories": {
                            "Disposable Instruments": {
                                "description": "Single-use surgical tools",
                                "subcategories": {}
                            },
                            "Robotic Surgery Systems": {
                                "description": "Robotics-assisted surgical platforms",
                                "subcategories": {}
                            },
                            "Implantable Devices": {
                                "description": "Devices implanted in the body (e.g., pacemakers)",
                                "subcategories": {}
                            }
                        }
                    },
                    "Wearable Health Trackers": {
                        "description": "Devices worn to monitor health metrics",
                        "subcategories": {
                            "Fitness Bands": {
                                "description": "Bands tracking steps, heart rate, etc.",
                                "subcategories": {}
                            },
                            "Smartwatches": {
                                "description": "Watches with health monitoring features",
                                "subcategories": {}
                            },
                            "Biosensors": {
                                "description": "Sensors measuring biological parameters",
                                "subcategories": {}
                            }
                        }
                    }
                }
            }
        }
    },
    "Engineering & Technology": {
        "description": "Engineering disciplines, IT, computing",
        "subcategories": {
            "Information Technology": {
                "description": "Software, AI, data analysis",
                "subcategories": {
                    "Software Development": {
                        "description": "Creating and maintaining software applications",
                        "subcategories": {
                            "Front-end Development": {
                                "description": "User interface and user experience",
                                "subcategories": {}
                            },
                            "Back-end Development": {
                                "description": "Server-side logic and databases",
                                "subcategories": {}
                            },
                            "Mobile App Development": {
                                "description": "Developing apps for mobile devices",
                                "subcategories": {}
                            }
                        }
                    },
                    "AI & Machine Learning": {
                        "description": "Developing models that learn from data",
                        "subcategories": {
                            "NLP": {
                                "description": "Natural language processing",
                                "subcategories": {}
                            },
                            "Computer Vision": {
                                "description": "Analyzing images and videos",
                                "subcategories": {}
                            },
                            "Recommendation Systems": {
                                "description": "Suggesting relevant items to users",
                                "subcategories": {}
                            }
                        }
                    },
                    "Cloud Computing": {
                        "description": "Delivering computing services over the internet",
                        "subcategories": {
                            "IaaS": {
                                "description": "Infrastructure as a Service",
                                "subcategories": {}
                            },
                            "PaaS": {
                                "description": "Platform as a Service",
                                "subcategories": {}
                            },
                            "SaaS": {
                                "description": "Software as a Service",
                                "subcategories": {}
                            }
                        }
                    }
                }
            },
            "Mechanical Engineering": {
                "description": "Mechanical systems, automotive, aerospace",
                "subcategories": {
                    "Automotive Engineering": {
                        "description": "Design and development of automobiles",
                        "subcategories": {
                            "Electric Vehicles": {
                                "description": "Battery and hybrid electric cars",
                                "subcategories": {}
                            },
                            "Internal Combustion Engines": {
                                "description": "Traditional engine design",
                                "subcategories": {}
                            },
                            "Automotive Safety Systems": {
                                "description": "Airbags, ABS, and other safety features",
                                "subcategories": {}
                            }
                        }
                    },
                    "Aerospace Engineering": {
                        "description": "Designing aircraft and spacecraft",
                        "subcategories": {
                            "Aircraft Design": {
                                "description": "Fixed-wing and rotary aircraft",
                                "subcategories": {}
                            },
                            "Spacecraft Engineering": {
                                "description": "Satellites, space shuttles, and related tech",
                                "subcategories": {}
                            },
                            "Propulsion Systems": {
                                "description": "Engines and thrusters for flight",
                                "subcategories": {}
                            }
                        }
                    },
                    "Industrial Machinery": {
                        "description": "Machinery used in manufacturing and industry",
                        "subcategories": {
                            "Manufacturing Robots": {
                                "description": "Robotics in assembly lines",
                                "subcategories": {}
                            },
                            "CNC Machines": {
                                "description": "Computer-controlled machining tools",
                                "subcategories": {}
                            },
                            "Heavy Machinery": {
                                "description": "Cranes, bulldozers, and industrial equipment",
                                "subcategories": {}
                            }
                        }
                    }
                }
            },
            "Electronics & Communication": {
                "description": "Electronics manufacturing and communication systems",
                "subcategories": {
                    "Semiconductors": {
                        "description": "Chips and integrated circuits",
                        "subcategories": {
                            "Integrated Circuits": {
                                "description": "Microchips for various applications",
                                "subcategories": {}
                            },
                            "Microprocessors": {
                                "description": "CPUs for computers and devices",
                                "subcategories": {}
                            },
                            "Memory Chips": {
                                "description": "RAM, ROM, and storage chips",
                                "subcategories": {}
                            }
                        }
                    },
                    "Communication Systems": {
                        "description": "Telecom and data communication infrastructure",
                        "subcategories": {
                            "Telecom Equipment": {
                                "description": "Switches, routers, and telecom hardware",
                                "subcategories": {}
                            },
                            "Satellite Communication": {
                                "description": "Communication via satellites",
                                "subcategories": {}
                            },
                            "Optical Fiber Networks": {
                                "description": "High-speed data transfer via fiber optics",
                                "subcategories": {}
                            }
                        }
                    },
                    "Consumer Electronics": {
                        "description": "Electronics for end-users",
                        "subcategories": {
                            "Smartphones": {
                                "description": "Mobile phones with advanced OS and features",
                                "subcategories": {}
                            },
                            "Televisions": {
                                "description": "TV sets for entertainment",
                                "subcategories": {}
                            },
                            "Home Appliances": {
                                "description": "Refrigerators, washing machines, etc.",
                                "subcategories": {}
                            }
                        }
                    }
                }
            }
        }
    },
    "Finance & Business": {
        "description": "Financial services, investments, banking",
        "subcategories": {
            "Banking": {
                "description": "Retail, corporate, and digital banking",
                "subcategories": {
                    "Retail Banking": {
                        "description": "Services for individual customers",
                        "subcategories": {
                            "Checking Accounts": {
                                "description": "Everyday bank accounts",
                                "subcategories": {}
                            },
                            "Savings Accounts": {
                                "description": "Interest-bearing deposit accounts",
                                "subcategories": {}
                            },
                            "Credit Cards": {
                                "description": "Cards for credit-based purchases",
                                "subcategories": {}
                            }
                        }
                    },
                    "Corporate Banking": {
                        "description": "Services for businesses and corporations",
                        "subcategories": {
                            "Business Loans": {
                                "description": "Financing for business ventures",
                                "subcategories": {}
                            },
                            "Trade Finance": {
                                "description": "Financing international trade",
                                "subcategories": {}
                            },
                            "Cash Management": {
                                "description": "Managing liquidity and payments",
                                "subcategories": {}
                            }
                        }
                    },
                    "Digital Banking": {
                        "description": "Banking services delivered via digital channels",
                        "subcategories": {
                            "Mobile Payments": {
                                "description": "Payments via mobile devices",
                                "subcategories": {}
                            },
                            "Online Banking Platforms": {
                                "description": "Web-based banking services",
                                "subcategories": {}
                            },
                            "Digital Wallets": {
                                "description": "Virtual wallets for holding payment info",
                                "subcategories": {}
                            }
                        }
                    }
                }
            },
            "Investment": {
                "description": "Investing in equities, startups, and other assets",
                "subcategories": {
                    "Venture Capital": {
                        "description": "Funding early-stage and growth-stage startups",
                        "subcategories": {
                            "Early-Stage Startups": {
                                "description": "Seed and Series A investments",
                                "subcategories": {}
                            },
                            "Growth Equity": {
                                "description": "Investing in more mature startups",
                                "subcategories": {}
                            },
                            "Tech-Focused Funds": {
                                "description": "VC funds specializing in technology companies",
                                "subcategories": {}
                            }
                        }
                    },
                    "Private Equity": {
                        "description": "Buyouts, restructuring, and mezzanine financing",
                        "subcategories": {
                            "Buyouts": {
                                "description": "Acquisition of controlling interests",
                                "subcategories": {}
                            },
                            "Restructuring": {
                                "description": "Reorganizing companies financially",
                                "subcategories": {}
                            },
                            "Mezzanine Financing": {
                                "description": "Hybrid of debt and equity financing",
                                "subcategories": {}
                            }
                        }
                    },
                    "Stock Markets": {
                        "description": "Public exchanges trading equities and derivatives",
                        "subcategories": {
                            "Equities Trading": {
                                "description": "Buying and selling company shares",
                                "subcategories": {}
                            },
                            "Derivatives": {
                                "description": "Futures and options trading",
                                "subcategories": {}
                            },
                            "Market Indices": {
                                "description": "Benchmarks like S&P 500",
                                "subcategories": {}
                            }
                        }
                    }
                }
            },
            "Insurance": {
                "description": "Risk management via insurance policies",
                "subcategories": {
                    "Life Insurance": {
                        "description": "Coverage on an individual's life",
                        "subcategories": {
                            "Term Life": {
                                "description": "Coverage for a specified term",
                                "subcategories": {}
                            },
                            "Whole Life": {
                                "description": "Coverage for entire lifetime",
                                "subcategories": {}
                            },
                            "Annuities": {
                                "description": "Contract that provides regular payments",
                                "subcategories": {}
                            }
                        }
                    },
                    "Health Insurance": {
                        "description": "Coverage for medical expenses",
                        "subcategories": {
                            "Individual Health Plans": {
                                "description": "Plans for individual policyholders",
                                "subcategories": {}
                            },
                            "Group Health Plans": {
                                "description": "Coverage for employees of a company",
                                "subcategories": {}
                            },
                            "Medicare/Medicaid": {
                                "description": "Government-backed health coverage",
                                "subcategories": {}
                            }
                        }
                    },
                    "Property & Casualty": {
                        "description": "Coverage for property damage and liability",
                        "subcategories": {
                            "Home Insurance": {
                                "description": "Coverage for private residences",
                                "subcategories": {}
                            },
                            "Auto Insurance": {
                                "description": "Coverage for vehicles",
                                "subcategories": {}
                            },
                            "Commercial Property Insurance": {
                                "description": "Coverage for business properties",
                                "subcategories": {}
                            }
                        }
                    }
                }
            }
        }
    },
    "Education & Research": {
        "description": "Academic institutions, research organizations",
        "subcategories": {
            "Academic Research": {
                "description": "Universities, labs, fundamental and applied research",
                "subcategories": {
                    "Fundamental Sciences": {
                        "description": "Physics, chemistry, basic science research",
                        "subcategories": {
                            "Particle Physics": {
                                "description": "Study of fundamental particles",
                                "subcategories": {}
                            },
                            "Organic Chemistry": {
                                "description": "Chemistry of carbon-containing compounds",
                                "subcategories": {}
                            },
                            "Astrophysics": {
                                "description": "Study of stars, galaxies, universe",
                                "subcategories": {}
                            }
                        }
                    },
                    "Social Sciences": {
                        "description": "Economics, sociology, anthropology",
                        "subcategories": {
                            "Macroeconomics": {
                                "description": "Study of large-scale economic factors",
                                "subcategories": {}
                            },
                            "Political Science": {
                                "description": "Study of politics and government",
                                "subcategories": {}
                            },
                            "Cultural Anthropology": {
                                "description": "Study of cultural variation among humans",
                                "subcategories": {}
                            }
                        }
                    },
                    "Applied Sciences": {
                        "description": "Biotech, materials science, environmental research",
                        "subcategories": {
                            "Biotechnology": {
                                "description": "Use of living systems to develop products",
                                "subcategories": {}
                            },
                            "Nanotechnology": {
                                "description": "Manipulation of matter at the nanoscale",
                                "subcategories": {}
                            },
                            "Environmental Science": {
                                "description": "Study of environment and ecology",
                                "subcategories": {}
                            }
                        }
                    }
                }
            },
            "Educational Institutions": {
                "description": "Places of learning and teaching",
                "subcategories": {
                    "Universities": {
                        "description": "Higher education institutions",
                        "subcategories": {
                            "Public Universities": {
                                "description": "State-owned universities",
                                "subcategories": {}
                            },
                            "Private Universities": {
                                "description": "Privately funded universities",
                                "subcategories": {}
                            },
                            "Research-Intensive Institutes": {
                                "description": "Universities focused on research output",
                                "subcategories": {}
                            }
                        }
                    },
                    "Vocational Schools": {
                        "description": "Focused on specific trades and skills",
                        "subcategories": {
                            "Technical Schools": {
                                "description": "Technical and mechanical skill training",
                                "subcategories": {}
                            },
                            "Culinary Institutes": {
                                "description": "Training in culinary arts",
                                "subcategories": {}
                            },
                            "Apprenticeship Programs": {
                                "description": "Work-based learning with mentors",
                                "subcategories": {}
                            }
                        }
                    },
                    "Online Education Platforms": {
                        "description": "Web-based learning solutions",
                        "subcategories": {
                            "MOOCs": {
                                "description": "Massive Open Online Courses",
                                "subcategories": {}
                            },
                            "E-Learning Courses": {
                                "description": "Structured online courses",
                                "subcategories": {}
                            },
                            "Educational Apps": {
                                "description": "Mobile applications for learning",
                                "subcategories": {}
                            }
                        }
                    }
                }
            },
            "Professional Training & Certification": {
                "description": "Skills upgrade and official certifications",
                "subcategories": {
                    "Corporate Training": {
                        "description": "Training within corporations",
                        "subcategories": {
                            "Leadership Training": {
                                "description": "Developing management skills",
                                "subcategories": {}
                            },
                            "Technical Skill Development": {
                                "description": "Enhancing technical abilities",
                                "subcategories": {}
                            },
                            "Soft Skills Workshops": {
                                "description": "Communication and teamwork training",
                                "subcategories": {}
                            }
                        }
                    },
                    "Professional Certifications": {
                        "description": "Recognized credentials in various fields",
                        "subcategories": {
                            "Project Management (PMP)": {
                                "description": "PMI certification for project managers",
                                "subcategories": {}
                            },
                            "Financial Analysis (CFA)": {
                                "description": "Chartered Financial Analyst credential",
                                "subcategories": {}
                            },
                            "IT Certifications (AWS, Cisco)": {
                                "description": "Vendor-specific IT skills credentials",
                                "subcategories": {}
                            }
                        }
                    },
                    "Continuing Education": {
                        "description": "Ongoing education for professionals",
                        "subcategories": {
                            "Lifelong Learning Programs": {
                                "description": "Programs encouraging continuous learning",
                                "subcategories": {}
                            },
                            "Executive Education": {
                                "description": "Programs for senior executives",
                                "subcategories": {}
                            },
                            "Professional Seminars": {
                                "description": "Short, intensive educational sessions",
                                "subcategories": {}
                            }
                        }
                    }
                }
            }
        }
    }
}
