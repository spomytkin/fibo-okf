---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: loan regulatory requirement
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A regulatory requirement defined in regulations by a comsumer credit act or other legislation.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Presence of a loan regulatory requirement associated with a loan indicates that the loan is regulated by the UK
      Consumer credit act or the equivalent in continental Europe.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/ConsumerCreditProtectionLaw
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isMandatedBy
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/administeredBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Loan
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/regulates
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/LegalObligation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalObligation
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/LoanRegulatoryRequirement
sources:
- id: fibo-source-9d1d4cf0d4
  resource: references/fibo/LOAN/LoansGeneral/LoansRegulatory.rdf
  sha256: 9d1d4cf0d45e2966f6fbe27dd62486cdd11c427c2d40f7701ea8f1775769245b
  title: FIBO source LOAN/LoansGeneral/LoansRegulatory.rdf
title: loan regulatory requirement
type: Ontology Class
---

# loan regulatory requirement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/LoanRegulatoryRequirement>

## Definition

A regulatory requirement defined in regulations by a comsumer credit act or other legislation.

## Relationships

- **Subclass of**: [LegalObligation](/concepts/fibo/FND/Law/LegalCapacity/LegalObligation.md)

## Constraints

- **[isMandatedBy](/concepts/fibo/FND/Relations/Relations/isMandatedBy.md)**: some values from of type [ConsumerCreditProtectionLaw](/concepts/fibo/LOAN/LoansGeneral/LoansRegulatory/ConsumerCreditProtectionLaw.md)
- **[administeredBy](/concepts/fibo/LOAN/LoansGeneral/LoansRegulatory/administeredBy.md)**: some values from of type [RegulatoryAgency](<https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency>)
- **[regulates](<https://www.omg.org/spec/Commons/RegulatoryAgencies/regulates>)**: some values from of type [Loan](/concepts/fibo/LOAN/LoansGeneral/Loans/Loan.md)

## Annotations

- **label** (en): loan regulatory requirement
- **definition** (en): A regulatory requirement defined in regulations by a comsumer credit act or other legislation.
- **explanatoryNote** (en): Presence of a loan regulatory requirement associated with a loan indicates that the loan is regulated by the UK Consumer credit act or the equivalent in continental Europe.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
