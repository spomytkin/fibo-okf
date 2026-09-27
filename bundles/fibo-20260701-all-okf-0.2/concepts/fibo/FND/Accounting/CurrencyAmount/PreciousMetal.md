---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: precious metal
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: metal that is considered to be rare and/or have a high economic value
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasNumericCode
  - filler: http://www.w3.org/2001/XMLSchema#string
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/hasTextualName
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/Metal.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/Metal
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/NegotiableCommodity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/NegotiableCommodity
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/PreciousMetal
sources:
- id: fibo-source-e460829ab0
  resource: references/fibo/DER/DerivativesContracts/CommoditiesContracts.rdf
  sha256: e460829ab039670f9e06a5e2f7c8a0435a5c7529015e0dbe7a9a790464504bd8
  title: FIBO source DER/DerivativesContracts/CommoditiesContracts.rdf
- id: fibo-source-4355744519
  resource: references/fibo/FND/Accounting/CurrencyAmount.rdf
  sha256: 4355744519e448cbeeedd0e9601a43470dc1329a7cab73d807e7b99048db0032
  title: FIBO source FND/Accounting/CurrencyAmount.rdf
- id: fibo-source-7f330c2b6d
  resource: references/fibo/FND/ProductsAndServices/ProductsAndServices.rdf
  sha256: 7f330c2b6de4e90f2c5d728ddf32af1d75f320646040450c1da9a8c5f8740548
  title: FIBO source FND/ProductsAndServices/ProductsAndServices.rdf
title: precious metal
type: Ontology Class
---

# precious metal

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/PreciousMetal>

## Definition

metal that is considered to be rare and/or have a high economic value

## Relationships

- **Subclass of**: [Metal](/concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/Metal.md)
- **Subclass of**: [NegotiableCommodity](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/NegotiableCommodity.md)

## Constraints

- **[hasNumericCode](/concepts/fibo/FND/Accounting/CurrencyAmount/hasNumericCode.md)**: exact qualified cardinality 1 of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[hasTextualName](<https://www.omg.org/spec/Commons/Designators/hasTextualName>)**: some values from of type [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label**: precious metal
- **definition**: metal that is considered to be rare and/or have a high economic value

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
