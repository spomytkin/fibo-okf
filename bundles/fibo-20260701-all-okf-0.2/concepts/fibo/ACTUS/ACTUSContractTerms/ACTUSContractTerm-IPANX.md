---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - IPANX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: cycleAnchorDateOfInterestPayment
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: Date from which the interest payment date schedule is calculated according to the cycle length. The first interest
      payment event takes place on this anchor.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: IPANX
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Cycle Anchor Date Of Interest Payment
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Interest.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Interest
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-IPANX
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - IPANX
type: Ontology Individual
---

# ACTUS contract term - IPANX

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-IPANX>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Interest](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Interest.md)

## Annotations

- **label**: ACTUS contract term - IPANX
- **hasParameterName**: cycleAnchorDateOfInterestPayment
- **hasDescription**: Date from which the interest payment date schedule is calculated according to the cycle length. The first interest payment event takes place on this anchor.
- **hasTag**: IPANX
- **hasTextualName**: Cycle Anchor Date Of Interest Payment

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
