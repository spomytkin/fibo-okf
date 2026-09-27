---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: loan participation note
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit facility and fixed-income security that may be distributed across a group of lenders
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: LPN
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The main difference between a loan participation and a loan syndication is that in a loan participation, one lender
      sells ownership interests in a loan to other lenders, while in a loan syndication, the lenders work together to originate
      and lend on the loan.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: With an LPN, a lead bank underwrites and issues the loan. This lending institution then recruits other banks to
      participate and share the risks and profits on a pro rata basis. The lead lender keeps a partial interest in the loan
      and is responsible for servicing it.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DistributedLoans/LeadArranger
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasActor
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CreditFacility.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditFacility
  - concept: /concepts/fibo/LOAN/LoansSpecific/CommercialLoans/CommercialLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CommercialLoans/CommercialLoan
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/FixedIncomeSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/FixedIncomeSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DistributedLoans/LoanParticipationNote
sources:
- id: fibo-source-e5c52f2c6a
  resource: references/fibo/SEC/Debt/DistributedLoans.rdf
  sha256: e5c52f2c6a506f223eaf08eee9562afee227c14cccfe925edbce3b2eeaa074b0
  title: FIBO source SEC/Debt/DistributedLoans.rdf
title: loan participation note
type: Ontology Class
---

# loan participation note

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DistributedLoans/LoanParticipationNote>

## Definition

credit facility and fixed-income security that may be distributed across a group of lenders

## Relationships

- **Subclass of**: [CreditFacility](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditFacility.md)
- **Subclass of**: [CommercialLoan](/concepts/fibo/LOAN/LoansSpecific/CommercialLoans/CommercialLoan.md)
- **Subclass of**: [FixedIncomeSecurity](/concepts/fibo/SEC/Debt/DebtInstruments/FixedIncomeSecurity.md)

## Constraints

- **[hasActor](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasActor>)**: exact qualified cardinality 1 of type [LeadArranger](/concepts/fibo/SEC/Debt/DistributedLoans/LeadArranger.md)

## Annotations

- **label** (en): loan participation note
- **definition** (en): credit facility and fixed-income security that may be distributed across a group of lenders
- **abbreviation** (en): LPN
- **explanatoryNote** (en): The main difference between a loan participation and a loan syndication is that in a loan participation, one lender sells ownership interests in a loan to other lenders, while in a loan syndication, the lenders work together to originate and lend on the loan.
- **explanatoryNote** (en): With an LPN, a lead bank underwrites and issues the loan. This lending institution then recruits other banks to participate and share the risks and profits on a pro rata basis. The lead lender keeps a partial interest in the loan and is responsible for servicing it.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
