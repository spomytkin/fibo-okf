---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - IPDC
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: dayCountConvention
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: Method defining how days are counted between two dates. This finally defines the year fraction in accrual calculations.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: IPDC
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Day Count Convention
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Interest.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Interest
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-IPDC
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - IPDC
type: Ontology Individual
---

# ACTUS contract term - IPDC

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-IPDC>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Interest](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Interest.md)

## Annotations

- **label**: ACTUS contract term - IPDC
- **hasParameterName**: dayCountConvention
- **hasDescription**: Method defining how days are counted between two dates. This finally defines the year fraction in accrual calculations.
- **hasTag**: IPDC
- **hasTextualName**: Day Count Convention

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
