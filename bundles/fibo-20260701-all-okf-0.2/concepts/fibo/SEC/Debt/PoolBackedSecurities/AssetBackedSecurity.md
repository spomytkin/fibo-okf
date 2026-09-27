---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: asset-backed security
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: debt instrument backed by receivables other than those arising out of real estate loans or mortgages
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: ABS
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of Financial Instruments (CFI code), Fourth
      edition, 2019-10-01
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An asset-backed security (ABS) is a type of financial investment that is collateralized by an underlying pool of
      assets—usually ones that generate a cash flow from debt, such as loans, leases, credit card balances, or receivables.
      It takes the form of a bond or note, paying income at a fixed rate for a set amount of time, until maturity. ABS are
      financial securities backed by income-generating assets such as credit card receivables, home equity loans, student
      loans, and auto loans. Pooling assets into an ABS is a process called securitization. One difference between an ABS
      and a collateralized debt obligation (CDO) is that the CDO issuer is generally a special purpose vehicle (SPV) or trust.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Asset-backed securities, for example home equity loans (HEL), credit cards, and so forth are backed by receivables
      [payments] that are either secured (such as HEL) or unsecured (for example, credit cards). They are typically tranched
      based on default risk.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TrancheType
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/hasTrancheType
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/PoolBackedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/PoolBackedSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
- id: fibo-source-4922b5d6fd
  resource: references/fibo/SEC/Debt/PoolBackedSecurities.rdf
  sha256: 4922b5d6fd80f046fedb705a51e5978f5d67d714330601c4fa251be149c7b5c7
  title: FIBO source SEC/Debt/PoolBackedSecurities.rdf
title: asset-backed security
type: Ontology Class
---

# asset-backed security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity>

## Definition

debt instrument backed by receivables other than those arising out of real estate loans or mortgages

## Relationships

- **Subclass of**: [PoolBackedSecurity](/concepts/fibo/SEC/Debt/PoolBackedSecurities/PoolBackedSecurity.md)

## Constraints

- **Disjoint with**: [MortgageBackedSecurity](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity.md)
- **[hasTrancheType](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/hasTrancheType.md)**: some values from of type [TrancheType](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TrancheType.md)

## Annotations

- **label** (en): asset-backed security
- **definition** (en): debt instrument backed by receivables other than those arising out of real estate loans or mortgages
- **abbreviation** (en): ABS
- **adaptedFrom**: ISO 10962, Securities and related financial instruments - Classification of Financial Instruments (CFI code), Fourth edition, 2019-10-01
- **explanatoryNote** (en): An asset-backed security (ABS) is a type of financial investment that is collateralized by an underlying pool of assets—usually ones that generate a cash flow from debt, such as loans, leases, credit card balances, or receivables. It takes the form of a bond or note, paying income at a fixed rate for a set amount of time, until maturity. ABS are financial securities backed by income-generating assets such as credit card receivables, home equity loans, student loans, and auto loans. Pooling assets into an ABS is a process called securitization. One difference between an ABS and a collateralized debt obligation (CDO) is that the CDO issuer is generally a special purpose vehicle (SPV) or trust.
- **explanatoryNote** (en): Asset-backed securities, for example home equity loans (HEL), credit cards, and so forth are backed by receivables [payments] that are either secured (such as HEL) or unsecured (for example, credit cards). They are typically tranched based on default risk.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
