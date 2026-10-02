---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has offering
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates something to a voluntary but conditional promise submitted by a buyer or seller (offeror) to another (offeree)
      for acceptance, and which becomes legally enforceable if accepted by the offeree
  inverse_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/isOfferingOf.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/isOfferingOf
  range:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Offering.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Offering
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasOffering
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: has offering
type: Ontology Property
---

# has offering

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasOffering>

## Definition

relates something to a voluntary but conditional promise submitted by a buyer or seller (offeror) to another (offeree) for acceptance, and which becomes legally enforceable if accepted by the offeree

## Relationships

- **Inverse of**: [isOfferingOf](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/isOfferingOf.md)
- **Range**: [Offering](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Offering.md)

## Annotations

- **label**: has offering
- **definition**: relates something to a voluntary but conditional promise submitted by a buyer or seller (offeror) to another (offeree) for acceptance, and which becomes legally enforceable if accepted by the offeree

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
