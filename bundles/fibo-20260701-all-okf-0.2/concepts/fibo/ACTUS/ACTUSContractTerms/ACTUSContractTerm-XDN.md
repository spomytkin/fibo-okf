---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - XDN
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: xDayNotice
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: Used as rolling attribute with the callable CT's UMP and CLM uniquely. CLM's and UMP's will not be settled (MD
      not set) until the client uses his option to call the contract X_Day_Notice after Current Date. As long as MD or TD
      is not set, the client postpones his right to call to the future. The cycle is normally defined in number of business
      days.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: XDN
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: X Day Notice
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-XDN
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - XDN
type: Ontology Individual
---

# ACTUS contract term - XDN

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-XDN>

## Relationships

- **Related to**: [ACTUSContractTermGroup-NotionalPrincipal](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal.md)

## Annotations

- **label**: ACTUS contract term - XDN
- **hasParameterName**: xDayNotice
- **hasDescription**: Used as rolling attribute with the callable CT's UMP and CLM uniquely. CLM's and UMP's will not be settled (MD not set) until the client uses his option to call the contract X_Day_Notice after Current Date. As long as MD or TD is not set, the client postpones his right to call to the future. The cycle is normally defined in number of business days.
- **hasTag**: XDN
- **hasTextualName**: X Day Notice

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
