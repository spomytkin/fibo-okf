---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: consumer credit requirement
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Requirement set out on the lender about how they must treat the appliction to a loan
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: e..g being able to see and challenge information about them held by the credit agency or lender. e.g. can't publish
      opinions only facts, etc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/ConsumerRight
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/confers
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/ConsumerProtectionAgency
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/overseenBy
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/LegalObligation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalObligation
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/ConsumerCreditRequirement
sources:
- id: fibo-source-9d1d4cf0d4
  resource: references/fibo/LOAN/LoansGeneral/LoansRegulatory.rdf
  sha256: 9d1d4cf0d45e2966f6fbe27dd62486cdd11c427c2d40f7701ea8f1775769245b
  title: FIBO source LOAN/LoansGeneral/LoansRegulatory.rdf
title: consumer credit requirement
type: Ontology Class
---

# consumer credit requirement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/ConsumerCreditRequirement>

## Definition

Requirement set out on the lender about how they must treat the appliction to a loan

## Relationships

- **Subclass of**: [LegalObligation](/concepts/fibo/FND/Law/LegalCapacity/LegalObligation.md)

## Constraints

- **[confers](/concepts/fibo/FND/Relations/Relations/confers.md)**: some values from of type [ConsumerRight](/concepts/fibo/LOAN/LoansGeneral/LoansRegulatory/ConsumerRight.md)
- **[overseenBy](/concepts/fibo/LOAN/LoansGeneral/LoansRegulatory/overseenBy.md)**: some values from of type [ConsumerProtectionAgency](/concepts/fibo/LOAN/LoansGeneral/LoansRegulatory/ConsumerProtectionAgency.md)

## Annotations

- **label** (en): consumer credit requirement
- **definition** (en): Requirement set out on the lender about how they must treat the appliction to a loan
- **explanatoryNote** (en): e..g being able to see and challenge information about them held by the credit agency or lender. e.g. can't publish opinions only facts, etc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
