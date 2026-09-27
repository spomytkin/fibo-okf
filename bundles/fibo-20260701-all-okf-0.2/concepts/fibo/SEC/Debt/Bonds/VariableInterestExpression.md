---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: variable interest expression
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an expression used to determine a variable interest payment amount
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasCeiling
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasFloor
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/FullyIndexedInterestRate
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableInterestExpression
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: variable interest expression
type: Ontology Class
---

# variable interest expression

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableInterestExpression>

## Definition

an expression used to determine a variable interest payment amount

## Relationships

- **Subclass of**: [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Constraints

- **[hasCeiling](/concepts/fibo/SEC/Debt/Bonds/hasCeiling.md)**: max qualified cardinality 1 of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **[hasFloor](/concepts/fibo/SEC/Debt/Bonds/hasFloor.md)**: max qualified cardinality 1 of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: exact qualified cardinality 1 of type [FullyIndexedInterestRate](/concepts/fibo/SEC/Debt/DebtInstruments/FullyIndexedInterestRate.md)

## Annotations

- **label**: variable interest expression
- **definition**: an expression used to determine a variable interest payment amount

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
