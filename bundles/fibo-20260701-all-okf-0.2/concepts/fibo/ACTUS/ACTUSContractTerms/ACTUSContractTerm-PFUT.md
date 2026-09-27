---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - PFUT
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: futuresPrice
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: 'The price the counterparties agreed upon at which the underlying contract (of a FUTUR) is exchanged/settled at
      STD. Quoting is different for different types of underlyings: Fixed Income = in percentage, all others in nominal terms.'
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: PFUT
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Futures Price
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Settlement.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Settlement
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-PFUT
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - PFUT
type: Ontology Individual
---

# ACTUS contract term - PFUT

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-PFUT>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Settlement](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Settlement.md)

## Annotations

- **label**: ACTUS contract term - PFUT
- **hasParameterName**: futuresPrice
- **hasDescription**: The price the counterparties agreed upon at which the underlying contract (of a FUTUR) is exchanged/settled at STD. Quoting is different for different types of underlyings: Fixed Income = in percentage, all others in nominal terms.
- **hasTag**: PFUT
- **hasTextualName**: Futures Price

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
