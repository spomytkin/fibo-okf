---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Regulation S
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: securities regulation defining an exemption through which corporations can issue unregistered securities to qualified
      foreign investors and foreign institutions
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Regulation S is defined in the US Code of Federal Regulations (CFR) Title 17, Chapter II, Part 230, clauses 901-905.
      See https://www.ecfr.gov/current/title-17/chapter-II/part-230?toc=1 for the actual text of the regulation.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Regulation S covers rules governing offers and sales made outside the United States without registration under
      the Securities Act of 1933. Created in 1990, this regulation was intended to encourage foreign investors to purchase
      American stocks in order to increase the liquidity of American markets.
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/InvestorsDomicileRestriction
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/QualifiedInvestorRestriction
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/SecuritiesRegulation
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction.md
    predicate: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.sec.gov/divisions/corpfin/ecfrlinks
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/RegulationS
sources:
- id: fibo-source-91c51c4810
  resource: references/fibo/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions.rdf
  sha256: 91c51c4810cfe6c5acc0aaf99de529357298d47f01cfe4f5eee4962f40f5be33
  title: FIBO source SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions.rdf
title: Regulation S
type: Ontology Individual
---

# Regulation S

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/RegulationS>

## Definition

securities regulation defining an exemption through which corporations can issue unregistered securities to qualified foreign investors and foreign institutions

## Relationships

- **Related to**: [UnitedStatesJurisdiction](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction.md)
- **See also**: [ecfrlinks](<https://www.sec.gov/divisions/corpfin/ecfrlinks>)

## Annotations

- **label**: Regulation S
- **definition**: securities regulation defining an exemption through which corporations can issue unregistered securities to qualified foreign investors and foreign institutions
- **adaptedFrom**: Regulation S is defined in the US Code of Federal Regulations (CFR) Title 17, Chapter II, Part 230, clauses 901-905. See https://www.ecfr.gov/current/title-17/chapter-II/part-230?toc=1 for the actual text of the regulation.
- **explanatoryNote**: Regulation S covers rules governing offers and sales made outside the United States without registration under the Securities Act of 1933. Created in 1990, this regulation was intended to encourage foreign investors to purchase American stocks in order to increase the liquidity of American markets.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
