---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - DVEX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: exDividendDate
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: In case contract is traded between DVEX and next DV payment date (i.e. PRD>DVEX & PRD<next DV payment date), then
      the old holder of the contract (previous to the trade) receives the next DV payment. In other words, the next DV payment
      is cancelled for the new (after the trade) holder of the contract.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: DVEX
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Ex Dividend Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Dividend.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Dividend
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-DVEX
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - DVEX
type: Ontology Individual
---

# ACTUS contract term - DVEX

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-DVEX>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Dividend](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Dividend.md)

## Annotations

- **label**: ACTUS contract term - DVEX
- **hasParameterName**: exDividendDate
- **hasDescription**: In case contract is traded between DVEX and next DV payment date (i.e. PRD>DVEX & PRD<next DV payment date), then the old holder of the contract (previous to the trade) receives the next DV payment. In other words, the next DV payment is cancelled for the new (after the trade) holder of the contract.
- **hasTag**: DVEX
- **hasTextualName**: Ex Dividend Date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
