---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: commercial loan
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: loan extended to a corporation, commercial enterprise, joint venture, or other organization as opposed to a consumer
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Such loans may include those that provide working capital, are used to finance the purchase of equipment and/or
      materials, for facilities and/or improvement of facilities, and so forth, and are typically secured.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: commercial and industrial loan
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasBorrower
    value: Nfc929016f55144119a05df5959575bdb
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/BusinessObjective
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasObjective
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CommercialLoans/hasBusinessPurposeDescription
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans/Loan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Loan
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CommercialLoans/CommercialLoan
sources:
- id: fibo-source-c2843be0fa
  resource: references/fibo/LOAN/LoansSpecific/CommercialLoans.rdf
  sha256: c2843be0fac87b4f6ea4a3f88fe40c64784f8800a75ccdb185bbd2265d9bd7c3
  title: FIBO source LOAN/LoansSpecific/CommercialLoans.rdf
title: commercial loan
type: Ontology Class
---

# commercial loan

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CommercialLoans/CommercialLoan>

## Definition

loan extended to a corporation, commercial enterprise, joint venture, or other organization as opposed to a consumer

## Relationships

- **Subclass of**: [Loan](/concepts/fibo/LOAN/LoansGeneral/Loans/Loan.md)

## Constraints

- **[hasBorrower](/concepts/fibo/FBC/DebtAndEquities/Debt/hasBorrower.md)**: some values from value `Nfc929016f55144119a05df5959575bdb`
- **[hasObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasObjective.md)**: min qualified cardinality 0 of type [BusinessObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/BusinessObjective.md)
- **[hasBusinessPurposeDescription](/concepts/fibo/LOAN/LoansSpecific/CommercialLoans/hasBusinessPurposeDescription.md)**: min qualified cardinality 0 of type [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label** (en): commercial loan
- **definition** (en): loan extended to a corporation, commercial enterprise, joint venture, or other organization as opposed to a consumer
- **explanatoryNote** (en): Such loans may include those that provide working capital, are used to finance the purchase of equipment and/or materials, for facilities and/or improvement of facilities, and so forth, and are typically secured.
- **synonym** (en): commercial and industrial loan

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
