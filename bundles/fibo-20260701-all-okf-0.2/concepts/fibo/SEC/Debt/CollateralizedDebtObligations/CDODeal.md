---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: c d o deal
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: An Issue of a set of CDO tranches as part of an offering to the market.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Multiple tranches of securities are issued by the CDO issue (usually referred to simply as the CDO), offering investors
      various maturity and credit risk characteristics. Note that it is in the sense of CDO as an issue that one might say
      that a CDO "has tranches". The CDO as an individual instrument (labelled CDO in this model) does not have tranches but
      is itself a member of one or another tranche.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDOPortfolio
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/MezzanineCDOTranche
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/SeniorCDOTranche
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/SubordinatedCDOEquity
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/SuperSeniorCDOTranche
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDOPortfolioManager
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isManagedBy
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/DebtOffering.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/DebtOffering
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDODeal
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: c d o deal
type: Ontology Class
---

# c d o deal

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDODeal>

## Definition

An Issue of a set of CDO tranches as part of an offering to the market.

## Relationships

- **Subclass of**: [DebtOffering](/concepts/fibo/SEC/Debt/DebtInstruments/DebtOffering.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [CDOPortfolio](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDOPortfolio.md)
- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [MezzanineCDOTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/MezzanineCDOTranche.md)
- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [SeniorCDOTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/SeniorCDOTranche.md)
- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [SubordinatedCDOEquity](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/SubordinatedCDOEquity.md)
- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [SuperSeniorCDOTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/SuperSeniorCDOTranche.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [CollateralizedDebtObligation](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation.md)
- **[isManagedBy](<https://www.omg.org/spec/Commons/Organizations/isManagedBy>)**: some values from of type [CDOPortfolioManager](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDOPortfolioManager.md)

## Annotations

- **label** (en): c d o deal
- **definition** (en): An Issue of a set of CDO tranches as part of an offering to the market.
- **explanatoryNote** (en): Multiple tranches of securities are issued by the CDO issue (usually referred to simply as the CDO), offering investors various maturity and credit risk characteristics. Note that it is in the sense of CDO as an issue that one might say that a CDO "has tranches". The CDO as an individual instrument (labelled CDO in this model) does not have tranches but is itself a member of one or another tranche.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
