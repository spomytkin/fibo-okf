---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has registered agent
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies a party as one that has the legal, medical or financial capacity to act on behalf of someone else under
      specific circumstances
  range:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/LegalAgent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/LegalAgent
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasLegalAgent
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: has registered agent
type: Ontology Property
---

# has registered agent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasLegalAgent>

## Definition

identifies a party as one that has the legal, medical or financial capacity to act on behalf of someone else under specific circumstances

## Relationships

- **Range**: [LegalAgent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/LegalAgent.md)
- **Subproperty of**: [hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)

## Annotations

- **label**: has registered agent
- **definition**: identifies a party as one that has the legal, medical or financial capacity to act on behalf of someone else under specific circumstances

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
