---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: exposes in
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the state of affairs in which exposure occurs
  domain:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Exposure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Exposure
  range:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureSituation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureSituation
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/undergoes
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/exposesIn
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: exposes in
type: Ontology Property
---

# exposes in

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/exposesIn>

## Definition

indicates the state of affairs in which exposure occurs

## Relationships

- **Domain**: [Exposure](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Exposure.md)
- **Range**: [ExposureSituation](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureSituation.md)
- **Subproperty of**: [undergoes](<https://www.omg.org/spec/Commons/PartiesAndSituations/undergoes>)

## Annotations

- **label**: exposes in
- **definition**: indicates the state of affairs in which exposure occurs

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
