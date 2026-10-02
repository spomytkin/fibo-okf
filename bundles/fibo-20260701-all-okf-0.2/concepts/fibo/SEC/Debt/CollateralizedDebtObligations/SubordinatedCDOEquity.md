---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: subordinated c d o equity
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The subordinated (also known as equity) CDO tranche is the most junior tranche in the CDO issue. If there are defaults
      or the CDO's collateral otherwise underperforms, scheduled payments to senior and mezzanine tranches take precedence
      over those to subordinated/equity tranches.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This is not a tranche of the debt in the CDO but an equity interest in the pool of underlying. There is a very
      bottom piece, not a tranche, but rather called the preferred shares (or just pref shares, or equity) that is the very
      bottom most layer in a CDO and is also referred to as the "first loss piece" since, like equity in a corporation, losses
      are incurred here before any of the actual bond holders take losses. This isn't a tranche
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/SubordinatedCDOEquity
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: subordinated c d o equity
type: Ontology Class
---

# subordinated c d o equity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/SubordinatedCDOEquity>

## Definition

The subordinated (also known as equity) CDO tranche is the most junior tranche in the CDO issue. If there are defaults or the CDO's collateral otherwise underperforms, scheduled payments to senior and mezzanine tranches take precedence over those to subordinated/equity tranches.

## Relationships

- **Subclass of**: [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)

## Annotations

- **label** (en): subordinated c d o equity
- **definition** (en): The subordinated (also known as equity) CDO tranche is the most junior tranche in the CDO issue. If there are defaults or the CDO's collateral otherwise underperforms, scheduled payments to senior and mezzanine tranches take precedence over those to subordinated/equity tranches.
- **explanatoryNote** (en): This is not a tranche of the debt in the CDO but an equity interest in the pool of underlying. There is a very bottom piece, not a tranche, but rather called the preferred shares (or just pref shares, or equity) that is the very bottom most layer in a CDO and is also referred to as the "first loss piece" since, like equity in a corporation, losses are incurred here before any of the actual bond holders take losses. This isn't a tranche

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
