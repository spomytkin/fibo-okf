---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has exposed party
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the party subject to influence or risk in
  domain:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureSituation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureSituation
  inverse_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/isExposedPartyIn.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/isExposedPartyIn
  range:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureBearer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureBearer
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/hasActor
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasExposedParty
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: has exposed party
type: Ontology Property
---

# has exposed party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasExposedParty>

## Definition

indicates the party subject to influence or risk in

## Relationships

- **Domain**: [ExposureSituation](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureSituation.md)
- **Inverse of**: [isExposedPartyIn](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/isExposedPartyIn.md)
- **Range**: [ExposureBearer](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ExposureBearer.md)
- **Subproperty of**: [hasActor](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasActor>)

## Annotations

- **label**: has exposed party
- **definition**: indicates the party subject to influence or risk in

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
