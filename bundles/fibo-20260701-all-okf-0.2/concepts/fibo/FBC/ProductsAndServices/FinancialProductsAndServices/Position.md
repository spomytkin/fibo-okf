---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: position
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial exposure resulting from owning, borrowing, shorting, or entering into a contract (e.g., derivatives)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A position can be long or short, and it can be in any asset class, such as stocks, bonds, futures, or options.
      A position can be open (current) or closed (past), but in general use, unless a position is specifically referred to
      as closed, the assumption is that it references an open position.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: "Regulators use 'position' when speaking about exposure with respect to \n- CFTC futures/options positions\n- Basel\
      \ risk-weighted exposures\n- Short-selling regulations (net short position)\n- Derivatives reporting (swap positions)\n\
      \nA position may exist without a holding (e.g., short sale, swap exposure). A holding always implies a long position,\
      \ but a position does not always imply a holding."
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialExposure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialExposure
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Position
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: position
type: Ontology Class
---

# position

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Position>

## Definition

financial exposure resulting from owning, borrowing, shorting, or entering into a contract (e.g., derivatives)

## Relationships

- **Subclass of**: [FinancialExposure](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialExposure.md)

## Annotations

- **label**: position
- **definition**: financial exposure resulting from owning, borrowing, shorting, or entering into a contract (e.g., derivatives)
- **explanatoryNote**: A position can be long or short, and it can be in any asset class, such as stocks, bonds, futures, or options. A position can be open (current) or closed (past), but in general use, unless a position is specifically referred to as closed, the assumption is that it references an open position.
- **explanatoryNote**: Regulators use 'position' when speaking about exposure with respect to  - CFTC futures/options positions - Basel risk-weighted exposures - Short-selling regulations (net short position) - Derivatives reporting (swap positions)  A position may exist without a holding (e.g., short sale, swap exposure). A holding always implies a long position, but a position does not always imply a holding.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
