---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has repayment terms
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the specific terms related to repayment of principal as specified in the instrument or a related contract
      document
  range:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasRepaymentTerms
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: has repayment terms
type: Ontology Property
---

# has repayment terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasRepaymentTerms>

## Definition

indicates the specific terms related to repayment of principal as specified in the instrument or a related contract document

## Relationships

- **Range**: [PrincipalRepaymentTerms](/concepts/fibo/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms.md)
- **Subproperty of**: [hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)

## Annotations

- **label**: has repayment terms
- **definition**: indicates the specific terms related to repayment of principal as specified in the instrument or a related contract document

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
