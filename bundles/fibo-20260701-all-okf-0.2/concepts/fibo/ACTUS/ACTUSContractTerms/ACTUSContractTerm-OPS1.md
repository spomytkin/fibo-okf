---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - OPS1
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: optionStrike1
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: 'Strike price of the option. Whether it is a call/put is determined by the attribute OPTP, i.e a call or a put
      (or a combination of call/put).


      This attribute is used for price related options such as options on bonds, stocks or FX. Interest rate related options
      (caps/floos) are handled within th RatReset group.'
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: OPS1
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Option Strike 1
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Optionality.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Optionality
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-OPS1
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - OPS1
type: Ontology Individual
---

# ACTUS contract term - OPS1

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-OPS1>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Optionality](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Optionality.md)

## Annotations

- **label**: ACTUS contract term - OPS1
- **hasParameterName**: optionStrike1
- **hasDescription**: Strike price of the option. Whether it is a call/put is determined by the attribute OPTP, i.e a call or a put (or a combination of call/put).  This attribute is used for price related options such as options on bonds, stocks or FX. Interest rate related options (caps/floos) are handled within th RatReset group.
- **hasTag**: OPS1
- **hasTextualName**: Option Strike 1

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
