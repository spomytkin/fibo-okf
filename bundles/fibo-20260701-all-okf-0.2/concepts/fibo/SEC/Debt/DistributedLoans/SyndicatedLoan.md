---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: syndicated loan
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit agreement in which a group of lenders, known as a syndicate, collectively provides a large loan to a single
      borrower
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A syndicated loan enables pooling of funds from multiple financial institutions, typically under the leadership
      of one or more arranging banks. These kinds of credit agreements are often used by large corporations, private equity
      investors and government entities for significant capital needs such as acquisitions, project financing, or to meet
      operational requirements.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasActor
    value: Na5bfd8cae8e7464fade6047324765ff6
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CreditFacility.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditFacility
  - concept: /concepts/fibo/LOAN/LoansSpecific/CommercialLoans/CommercialLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CommercialLoans/CommercialLoan
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DistributedLoans/SyndicatedLoan
sources:
- id: fibo-source-e5c52f2c6a
  resource: references/fibo/SEC/Debt/DistributedLoans.rdf
  sha256: e5c52f2c6a506f223eaf08eee9562afee227c14cccfe925edbce3b2eeaa074b0
  title: FIBO source SEC/Debt/DistributedLoans.rdf
title: syndicated loan
type: Ontology Class
---

# syndicated loan

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DistributedLoans/SyndicatedLoan>

## Definition

credit agreement in which a group of lenders, known as a syndicate, collectively provides a large loan to a single borrower

## Relationships

- **Subclass of**: [CreditFacility](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditFacility.md)
- **Subclass of**: [CommercialLoan](/concepts/fibo/LOAN/LoansSpecific/CommercialLoans/CommercialLoan.md)

## Constraints

- **[hasActor](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasActor>)**: some values from value `Na5bfd8cae8e7464fade6047324765ff6`

## Annotations

- **label** (en): syndicated loan
- **definition** (en): credit agreement in which a group of lenders, known as a syndicate, collectively provides a large loan to a single borrower
- **explanatoryNote** (en): A syndicated loan enables pooling of funds from multiple financial institutions, typically under the leadership of one or more arranging banks. These kinds of credit agreements are often used by large corporations, private equity investors and government entities for significant capital needs such as acquisitions, project financing, or to meet operational requirements.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
