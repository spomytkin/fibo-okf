---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: controlled amortization asset-backed security
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: asset-backed security based on a pool of bonds securitized using a controlled amortization structure
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.investinginbonds.com/learnmore.asp?catid=11&subcatid=57&id=15
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Controlled-amortization ABS resemble corporate bonds with a sinking fund. After a predetermined 'revolving' period
      during which only interest payments are made, these securities attempt to return principal to investors in a series
      of defined periodic payments that usually occur over less than a year.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Revolving debt (primarily credit card receivables, but also HELOCs, trade receivables, dealer floor-plan loans
      and some leases) may be securitized using a controlled amortization structure. This is a method of providing investors
      with a relatively predictable repayment schedule, even though the underlying assets are nonamortizing. A risk inherent
      in this kind of ABS is an early amortization event.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/DebtPool
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondAmortizationPaymentTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasRepaymentTerms
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/ControlledAmortizationAssetBackedSecurity
sources:
- id: fibo-source-bc31503fb4
  resource: references/fibo/SEC/Debt/AssetBackedSecurities.rdf
  sha256: bc31503fb47984eace3c48c15e458215440e108098254f13885985b958f90b44
  title: FIBO source SEC/Debt/AssetBackedSecurities.rdf
title: controlled amortization asset-backed security
type: Ontology Class
---

# controlled amortization asset-backed security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/ControlledAmortizationAssetBackedSecurity>

## Definition

asset-backed security based on a pool of bonds securitized using a controlled amortization structure

## Relationships

- **Subclass of**: [AssetBackedSecurity](/concepts/fibo/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md)

## Constraints

- **[isBasedOn](/concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md)**: some values from of type [DebtPool](/concepts/fibo/SEC/Securities/Pools/DebtPool.md)
- **[hasRepaymentTerms](/concepts/fibo/SEC/Debt/DebtInstruments/hasRepaymentTerms.md)**: some values from of type [BondAmortizationPaymentTerms](/concepts/fibo/SEC/Debt/Bonds/BondAmortizationPaymentTerms.md)

## Annotations

- **label**: controlled amortization asset-backed security
- **definition**: asset-backed security based on a pool of bonds securitized using a controlled amortization structure
- **adaptedFrom**: http://www.investinginbonds.com/learnmore.asp?catid=11&subcatid=57&id=15
- **explanatoryNote**: Controlled-amortization ABS resemble corporate bonds with a sinking fund. After a predetermined 'revolving' period during which only interest payments are made, these securities attempt to return principal to investors in a series of defined periodic payments that usually occur over less than a year.
- **explanatoryNote**: Revolving debt (primarily credit card receivables, but also HELOCs, trade receivables, dealer floor-plan loans and some leases) may be securitized using a controlled amortization structure. This is a method of providing investors with a relatively predictable repayment schedule, even though the underlying assets are nonamortizing. A risk inherent in this kind of ABS is an early amortization event.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
