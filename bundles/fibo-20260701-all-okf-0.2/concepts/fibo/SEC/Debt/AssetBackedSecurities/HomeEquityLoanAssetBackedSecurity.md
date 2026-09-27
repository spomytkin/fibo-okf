---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: home equity loan asset-backed security
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: asset-backed security based on home equity loan receivables
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: If the credit risk of the pool has been decoupled from the institution via an SPV, then home equity asset-backed
      securities are also structured finance instruments.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Similar to mortgages, home equity loans are often taken out by borrowers who have less-than-stellar credit scores
      or few assets - the reason why they didn’t qualify for a mortgage. These are amortizing loans - that is, payment goes
      toward satisfying a specific sum and consists of three categories: interest, principal, and prepayments.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/HomeEquityLineOfCreditPool
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/HomeEquityLoanAssetBackedSecurity
sources:
- id: fibo-source-bc31503fb4
  resource: references/fibo/SEC/Debt/AssetBackedSecurities.rdf
  sha256: bc31503fb47984eace3c48c15e458215440e108098254f13885985b958f90b44
  title: FIBO source SEC/Debt/AssetBackedSecurities.rdf
title: home equity loan asset-backed security
type: Ontology Class
---

# home equity loan asset-backed security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/HomeEquityLoanAssetBackedSecurity>

## Definition

asset-backed security based on home equity loan receivables

## Relationships

- **Subclass of**: [AssetBackedSecurity](/concepts/fibo/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md)

## Constraints

- **[isBasedOn](/concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md)**: some values from of type [HomeEquityLineOfCreditPool](/concepts/fibo/SEC/Debt/AssetBackedSecurities/HomeEquityLineOfCreditPool.md)

## Annotations

- **label** (en): home equity loan asset-backed security
- **definition** (en): asset-backed security based on home equity loan receivables
- **explanatoryNote** (en): If the credit risk of the pool has been decoupled from the institution via an SPV, then home equity asset-backed securities are also structured finance instruments.
- **explanatoryNote** (en): Similar to mortgages, home equity loans are often taken out by borrowers who have less-than-stellar credit scores or few assets - the reason why they didn’t qualify for a mortgage. These are amortizing loans - that is, payment goes toward satisfying a specific sum and consists of three categories: interest, principal, and prepayments.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
