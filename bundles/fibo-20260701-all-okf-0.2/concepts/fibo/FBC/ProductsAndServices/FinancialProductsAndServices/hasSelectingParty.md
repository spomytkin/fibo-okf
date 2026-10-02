---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has selecting party
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the person(s) or organization(s) responsible for determining the contents of a basket
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/hasParty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasSelectingParty
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: has selecting party
type: Ontology Property
---

# has selecting party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasSelectingParty>

## Definition

indicates the person(s) or organization(s) responsible for determining the contents of a basket

## Relationships

- **Range**: [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)
- **Subproperty of**: [hasParty](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasParty>)

## Annotations

- **label**: has selecting party
- **definition**: indicates the person(s) or organization(s) responsible for determining the contents of a basket

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
