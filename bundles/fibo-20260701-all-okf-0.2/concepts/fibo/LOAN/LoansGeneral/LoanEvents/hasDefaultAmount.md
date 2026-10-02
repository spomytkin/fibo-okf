---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has default amount
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: amount before the application of sale proceeds and recoveries
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Undefined PoC SDM Notes: Default or Foreclosure amount - Total default amount before the application of sale proceeds
      and recoveries.&nbsp; (AO 146, RR 135) Loan Default Proceeding_cd= (1) Default amount </p> <p> Sale price - Price achieved
      on sale of property ( AO 147, RR 137 )&nbsp; Loan Default Proceeding_cd= (2) Property Sale </p> <p> Loss on Sale&nbsp;&nbsp;
      Total loss net of fees, accrued interest etc. after application of sale proceeds (excluding prepayment charge if subordinate
      to principal recoveries). Show any gain on sale as a negative number (AO 148, RR 138 )&nbsp; Loan Default Proceeding_cd
      = (3) Loss amount </p> <p> Cumulative Reocveries - ony relevant for cases with losses&nbsp; ( AO 149, RR 139 )&nbsp;
      Loan Default Proceeding_cd =&nbsp; (4) Recoveries </p> <p> Professional Negligence Recoveries - Any amounts received
      in settlement or as a result of professional negligence claims against surveyors, solicitors etc. net of any fees /
      costs ( AO 150, RR 140 )&nbsp; Loan Default Proceeding_cd = (5) Professional Negligence </p><br />'
  domain:
  - concept: /concepts/fibo/LOAN/LoansGeneral/LoanEvents/LoanDefaultProceeding.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/LoanDefaultProceeding
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMonetaryAmount
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/hasDefaultAmount
sources:
- id: fibo-source-48fe43dc99
  resource: references/fibo/LOAN/LoansGeneral/LoanEvents.rdf
  sha256: 48fe43dc99b1d7ca56ee712ff80baad56b5ac6abd1e4cb8ac5342e7bdee88e6e
  title: FIBO source LOAN/LoansGeneral/LoanEvents.rdf
title: has default amount
type: Ontology Property
---

# has default amount

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/hasDefaultAmount>

## Definition

amount before the application of sale proceeds and recoveries

## Relationships

- **Domain**: [LoanDefaultProceeding](/concepts/fibo/LOAN/LoansGeneral/LoanEvents/LoanDefaultProceeding.md)
- **Range**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **Subproperty of**: [hasMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md)

## Annotations

- **label** (en): has default amount
- **definition** (en): amount before the application of sale proceeds and recoveries
- **explanatoryNote** (en): Undefined PoC SDM Notes: Default or Foreclosure amount - Total default amount before the application of sale proceeds and recoveries.&nbsp; (AO 146, RR 135) Loan Default Proceeding_cd= (1) Default amount </p> <p> Sale price - Price achieved on sale of property ( AO 147, RR 137 )&nbsp; Loan Default Proceeding_cd= (2) Property Sale </p> <p> Loss on Sale&nbsp;&nbsp; Total loss net of fees, accrued interest etc. after application of sale proceeds (excluding prepayment charge if subordinate to principal recoveries). Show any gain on sale as a negative number (AO 148, RR 138 )&nbsp; Loan Default Proceeding_cd = (3) Loss amount </p> <p> Cumulative Reocveries - ony relevant for cases with losses&nbsp; ( AO 149, RR 139 )&nbsp; Loan Default Proceeding_cd =&nbsp; (4) Recoveries </p> <p> Professional Negligence Recoveries - Any amounts received in settlement or as a result of professional negligence claims against surveyors, solicitors etc. net of any fees / costs ( AO 150, RR 140 )&nbsp; Loan Default Proceeding_cd = (5) Professional Negligence </p><br />

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
