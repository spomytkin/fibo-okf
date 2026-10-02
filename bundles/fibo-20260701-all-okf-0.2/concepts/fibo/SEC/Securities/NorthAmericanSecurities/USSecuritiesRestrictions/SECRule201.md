---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: SEC Rule 201
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: securities regulation that is part of Regulation SHO that is a circuit breaker limiting short sales to prevent
      them from causing a security's price to drop further after a significant decline
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.sec.gov/divisions/marketreg/rule201faq.htm
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: On February 26, 2010, the Commission adopted Rule 201 of Regulation SHO. Rule 201 restricts the price at which
      short sales may be effected when a stock has experienced significant downward price pressure. Rule 201 became effective
      on May 10, 2010. (Securities Exchange Act Release No. 61595 (Feb. 26, 2010), 75 FR 11232 (Mar. 10, 2010) ('Rule 201
      Adopting Release')). Compliance with the new rule is required as of February 28, 2011. (Securities Exchange Act Release
      No. 63247 (Nov. 4, 2010), 75 FR 68702 (Nov. 9, 2010)).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The Securities and Exchange Commission (SEC) short sale alternative uptick rule (Rule 201) requires the establishment
      of a short sale-related circuit breaker in the event a security's price decreases by ten percent or more from the previous
      day's closing price. Once activated, the short sale restriction will remain in effect for the remainder of the day as
      well as the following day. Values are A - 'Flag in Effect/Activated', C - 'Flag Continued' and N - 'Flag Not in Effect'.
      If not given the default is 'N - Flag Not in Effect'. When a stock is triggered, traders can only execute short sales
      of the stock above the National Best Bid (NBB) price.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: alternative uptick rule
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/SecuritiesRegulation
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/TradingRestriction
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction.md
    predicate: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/SECRule201
sources:
- id: fibo-source-91c51c4810
  resource: references/fibo/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions.rdf
  sha256: 91c51c4810cfe6c5acc0aaf99de529357298d47f01cfe4f5eee4962f40f5be33
  title: FIBO source SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions.rdf
title: SEC Rule 201
type: Ontology Individual
---

# SEC Rule 201

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/SECRule201>

## Definition

securities regulation that is part of Regulation SHO that is a circuit breaker limiting short sales to prevent them from causing a security's price to drop further after a significant decline

## Relationships

- **Related to**: [UnitedStatesJurisdiction](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction.md)

## Annotations

- **label**: SEC Rule 201
- **definition**: securities regulation that is part of Regulation SHO that is a circuit breaker limiting short sales to prevent them from causing a security's price to drop further after a significant decline
- **adaptedFrom**: https://www.sec.gov/divisions/marketreg/rule201faq.htm
- **explanatoryNote**: On February 26, 2010, the Commission adopted Rule 201 of Regulation SHO. Rule 201 restricts the price at which short sales may be effected when a stock has experienced significant downward price pressure. Rule 201 became effective on May 10, 2010. (Securities Exchange Act Release No. 61595 (Feb. 26, 2010), 75 FR 11232 (Mar. 10, 2010) ('Rule 201 Adopting Release')). Compliance with the new rule is required as of February 28, 2011. (Securities Exchange Act Release No. 63247 (Nov. 4, 2010), 75 FR 68702 (Nov. 9, 2010)).
- **explanatoryNote**: The Securities and Exchange Commission (SEC) short sale alternative uptick rule (Rule 201) requires the establishment of a short sale-related circuit breaker in the event a security's price decreases by ten percent or more from the previous day's closing price. Once activated, the short sale restriction will remain in effect for the remainder of the day as well as the following day. Values are A - 'Flag in Effect/Activated', C - 'Flag Continued' and N - 'Flag Not in Effect'. If not given the default is 'N - Flag Not in Effect'. When a stock is triggered, traders can only execute short sales of the stock above the National Best Bid (NBB) price.
- **synonym**: alternative uptick rule

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
