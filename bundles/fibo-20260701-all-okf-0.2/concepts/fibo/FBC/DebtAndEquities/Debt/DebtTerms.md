---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: debt terms
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract terms that specify the formal rights and obligations of borrower and lender under a contract in which
      funds are lent from the one party to the other
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: These may be terms in a loan contract (including for example a mortgage contract) or they may be the contractual
      terms of a debt security.
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualCommitment
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DebtTerms
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: debt terms
type: Ontology Class
---

# debt terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DebtTerms>

## Definition

contract terms that specify the formal rights and obligations of borrower and lender under a contract in which funds are lent from the one party to the other

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Subclass of**: [ContractualCommitment](/concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md)

## Annotations

- **label**: debt terms
- **definition**: contract terms that specify the formal rights and obligations of borrower and lender under a contract in which funds are lent from the one party to the other
- **explanatoryNote**: These may be terms in a loan contract (including for example a mortgage contract) or they may be the contractual terms of a debt security.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
