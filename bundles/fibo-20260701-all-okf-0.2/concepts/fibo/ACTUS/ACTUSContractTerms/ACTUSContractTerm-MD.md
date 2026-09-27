---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - MD
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: maturityDate
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: "Marks the contractual end of the lifecycle of a CT. Generally, date of the last cash flows. \n\nThis includes\
      \ normally a principal and an interest payment. Some Maturity CTs as perpetuals (PBN) do not have such a date. For variable\
      \ amortizing contracts of the ANN CT, this date might be less than the scheduled end of the contract (which is deduced\
      \ from the periodic payment amount \n\nPRNXT). In this case it balloons."
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: MD
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Maturity Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-MD
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - MD
type: Ontology Individual
---

# ACTUS contract term - MD

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-MD>

## Relationships

- **Related to**: [ACTUSContractTermGroup-NotionalPrincipal](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal.md)

## Annotations

- **label**: ACTUS contract term - MD
- **hasParameterName**: maturityDate
- **hasDescription**: Marks the contractual end of the lifecycle of a CT. Generally, date of the last cash flows.   This includes normally a principal and an interest payment. Some Maturity CTs as perpetuals (PBN) do not have such a date. For variable amortizing contracts of the ANN CT, this date might be less than the scheduled end of the contract (which is deduced from the periodic payment amount   PRNXT). In this case it balloons.
- **hasTag**: MD
- **hasTextualName**: Maturity Date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
