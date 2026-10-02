---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund holding
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: ownership interest in a fund, which may represented by fund units that confer financial rights and governance privileges
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/consistsOfNumberOfUnits
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundUnit
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Documents/refersTo
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/FinancialAsset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/FinancialAsset
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundHolding
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: fund holding
type: Ontology Class
---

# fund holding

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundHolding>

## Definition

ownership interest in a fund, which may represented by fund units that confer financial rights and governance privileges

## Relationships

- **Subclass of**: [FinancialAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/FinancialAsset.md)

## Constraints

- **[consistsOfNumberOfUnits](/concepts/fibo/BE/OwnershipAndControl/CorporateOwnership/consistsOfNumberOfUnits.md)**: min qualified cardinality 0 of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: min qualified cardinality 0 of type [FundUnit](/concepts/fibo/SEC/Funds/Funds/FundUnit.md)

## Annotations

- **label**: fund holding
- **definition**: ownership interest in a fund, which may represented by fund units that confer financial rights and governance privileges

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
