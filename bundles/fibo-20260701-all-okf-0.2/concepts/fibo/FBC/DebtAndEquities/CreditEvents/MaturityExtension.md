---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: maturity extension
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit event involving extension of payments beyond the original maturity date of the obligation
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: As stipulated in the terms and conditions for a bond, for example, the issuer or the bondholder may prolong the
      maturity date. After extension, the security may differ from original issue (new rate or maturity date). May be subject
      to bondholder's approval.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/CorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/CorporateAction
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditEvents/ObligationSpecificCreditEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/ObligationSpecificCreditEvent
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/MaturityExtension
sources:
- id: fibo-source-690895114a
  resource: references/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
  sha256: 690895114a0787da52d8b7a7d29be50450d25041659e04b33e16f727ba350a92
  title: FIBO source CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
- id: fibo-source-bc069e913f
  resource: references/fibo/FBC/DebtAndEquities/CreditEvents.rdf
  sha256: bc069e913f78f120d461cf77899be0452acda5d5786c9cd342e37931a2b141c6
  title: FIBO source FBC/DebtAndEquities/CreditEvents.rdf
title: maturity extension
type: Ontology Class
---

# maturity extension

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/MaturityExtension>

## Definition

credit event involving extension of payments beyond the original maturity date of the obligation

## Relationships

- **Subclass of**: [CorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/CorporateAction.md)
- **Subclass of**: [ObligationSpecificCreditEvent](/concepts/fibo/FBC/DebtAndEquities/CreditEvents/ObligationSpecificCreditEvent.md)

## Annotations

- **label** (en): maturity extension
- **definition** (en): credit event involving extension of payments beyond the original maturity date of the obligation
- **explanatoryNote** (en): As stipulated in the terms and conditions for a bond, for example, the issuer or the bondholder may prolong the maturity date. After extension, the security may differ from original issue (new rate or maturity date). May be subject to bondholder's approval.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
