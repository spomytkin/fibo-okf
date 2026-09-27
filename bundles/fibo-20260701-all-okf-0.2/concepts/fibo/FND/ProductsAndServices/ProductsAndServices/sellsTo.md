---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: sells to
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: links a party in the role of broker, dealer, vendor, or merchandiser to a purchaser or potential purchasing party
  domain:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Seller.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Seller
  inverse_of:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/buysFrom.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/buysFrom
  range:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Buyer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Buyer
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/actsOn
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/sellsTo
sources:
- id: fibo-source-7f330c2b6d
  resource: references/fibo/FND/ProductsAndServices/ProductsAndServices.rdf
  sha256: 7f330c2b6de4e90f2c5d728ddf32af1d75f320646040450c1da9a8c5f8740548
  title: FIBO source FND/ProductsAndServices/ProductsAndServices.rdf
title: sells to
type: Ontology Property
---

# sells to

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/sellsTo>

## Definition

links a party in the role of broker, dealer, vendor, or merchandiser to a purchaser or potential purchasing party

## Relationships

- **Domain**: [Seller](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Seller.md)
- **Inverse of**: [buysFrom](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/buysFrom.md)
- **Range**: [Buyer](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Buyer.md)
- **Subproperty of**: [actsOn](<https://www.omg.org/spec/Commons/PartiesAndSituations/actsOn>)

## Annotations

- **label**: sells to
- **definition**: links a party in the role of broker, dealer, vendor, or merchandiser to a purchaser or potential purchasing party

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
