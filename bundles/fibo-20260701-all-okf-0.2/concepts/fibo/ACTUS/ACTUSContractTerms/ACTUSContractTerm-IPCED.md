---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - IPCED
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: capitalizationEndDate
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: If IPCED is set, then interest is not paid or received but added to the balance (NT) until IPCED. If IPCED does
      not coincide with an IP cycle, one additional interest payment gets calculated at IPCED and capitalized. Thereafter
      normal interest payments occur.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: IPCED
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Capitalization End Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Interest.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Interest
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-IPCED
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - IPCED
type: Ontology Individual
---

# ACTUS contract term - IPCED

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-IPCED>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Interest](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Interest.md)

## Annotations

- **label**: ACTUS contract term - IPCED
- **hasParameterName**: capitalizationEndDate
- **hasDescription**: If IPCED is set, then interest is not paid or received but added to the balance (NT) until IPCED. If IPCED does not coincide with an IP cycle, one additional interest payment gets calculated at IPCED and capitalized. Thereafter normal interest payments occur.
- **hasTag**: IPCED
- **hasTextualName**: Capitalization End Date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
