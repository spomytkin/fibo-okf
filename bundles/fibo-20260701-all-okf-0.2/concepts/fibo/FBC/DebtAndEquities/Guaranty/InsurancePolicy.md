---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: insurance policy
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract that (1) puts an indemnity cover into effect, (2) serves as a legal evidence of the insurance agreement,
      (3) sets out the exact terms on which the indemnity cover has been provided, and (4) states associated information such
      as the (a) specific risks and perils covered, (b) duration of coverage, (c) amount of premium, (d) mode of premium payment,
      and (e) deductibles, if any
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Policyholder
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasCounterparty
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Insurer
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/WrittenContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/InsurancePolicy
sources:
- id: fibo-source-a6bc9592ee
  resource: references/fibo/FBC/DebtAndEquities/Guaranty.rdf
  sha256: a6bc9592eeebb061e99b2dc168751d4b3612dbcc32c86c50959e17011e4247b0
  title: FIBO source FBC/DebtAndEquities/Guaranty.rdf
title: insurance policy
type: Ontology Class
---

# insurance policy

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/InsurancePolicy>

## Definition

contract that (1) puts an indemnity cover into effect, (2) serves as a legal evidence of the insurance agreement, (3) sets out the exact terms on which the indemnity cover has been provided, and (4) states associated information such as the (a) specific risks and perils covered, (b) duration of coverage, (c) amount of premium, (d) mode of premium payment, and (e) deductibles, if any

## Relationships

- **Subclass of**: [WrittenContract](/concepts/fibo/FND/Agreements/Contracts/WrittenContract.md)

## Constraints

- **[hasCounterparty](/concepts/fibo/FND/Agreements/Contracts/hasCounterparty.md)**: some values from of type [Policyholder](/concepts/fibo/FBC/DebtAndEquities/Guaranty/Policyholder.md)
- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: some values from of type [Insurer](/concepts/fibo/FBC/DebtAndEquities/Guaranty/Insurer.md)

## Annotations

- **label**: insurance policy
- **definition**: contract that (1) puts an indemnity cover into effect, (2) serves as a legal evidence of the insurance agreement, (3) sets out the exact terms on which the indemnity cover has been provided, and (4) states associated information such as the (a) specific risks and perils covered, (b) duration of coverage, (c) amount of premium, (d) mode of premium payment, and (e) deductibles, if any

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
