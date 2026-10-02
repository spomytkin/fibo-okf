---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - DS
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: deliverySettlement
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: 'Indicates whether the contract is settled in cash or physical delivery.


      In case of physical delivery, the underlying contract and associated (future) cash flows are effectively exchanged.
      In case of cash settlement, the current market value of the underlying contract determines the cash flow exchanged.'
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: DS
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Delivery Settlement
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Settlement.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Settlement
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-DS
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - DS
type: Ontology Individual
---

# ACTUS contract term - DS

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-DS>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Settlement](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Settlement.md)

## Annotations

- **label**: ACTUS contract term - DS
- **hasParameterName**: deliverySettlement
- **hasDescription**: Indicates whether the contract is settled in cash or physical delivery.  In case of physical delivery, the underlying contract and associated (future) cash flows are effectively exchanged. In case of cash settlement, the current market value of the underlying contract determines the cash flow exchanged.
- **hasTag**: DS
- **hasTextualName**: Delivery Settlement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
