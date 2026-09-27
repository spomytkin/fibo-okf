---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has buyer
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the purchasing party in the context of a sales transaction
  range:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Buyer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Buyer
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/hasUndergoer
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/hasBuyer
sources:
- id: fibo-source-7f330c2b6d
  resource: references/fibo/FND/ProductsAndServices/ProductsAndServices.rdf
  sha256: 7f330c2b6de4e90f2c5d728ddf32af1d75f320646040450c1da9a8c5f8740548
  title: FIBO source FND/ProductsAndServices/ProductsAndServices.rdf
title: has buyer
type: Ontology Property
---

# has buyer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/hasBuyer>

## Definition

indicates the purchasing party in the context of a sales transaction

## Relationships

- **Range**: [Buyer](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Buyer.md)
- **Subproperty of**: [hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)
- **Subproperty of**: [hasUndergoer](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasUndergoer>)

## Annotations

- **label** (en): has buyer
- **definition**: indicates the purchasing party in the context of a sales transaction

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
