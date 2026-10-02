---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Regulation D
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: securities regulation defining an exemption through which corporations do not have to register their securities
      and usually do not have to file reports with the SEC
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Regulation D is defined in the US Code of Federal Regulations (CFR) Title 17, Chapter II, Part 230, clauses 501-508.
      See https://www.ecfr.gov/current/title-17/chapter-II/part-230?toc=1 for the actual text of the regulation.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Issuers must file what's known as a 'Form D' after they first sell their securities if they qualify for registration
      under Regulation D.
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/SecuritiesRegulation
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction.md
    predicate: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.sec.gov/divisions/corpfin/ecfrlinks
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/RegulationD
sources:
- id: fibo-source-91c51c4810
  resource: references/fibo/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions.rdf
  sha256: 91c51c4810cfe6c5acc0aaf99de529357298d47f01cfe4f5eee4962f40f5be33
  title: FIBO source SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions.rdf
title: Regulation D
type: Ontology Individual
---

# Regulation D

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/RegulationD>

## Definition

securities regulation defining an exemption through which corporations do not have to register their securities and usually do not have to file reports with the SEC

## Relationships

- **Related to**: [UnitedStatesJurisdiction](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction.md)
- **See also**: [ecfrlinks](<https://www.sec.gov/divisions/corpfin/ecfrlinks>)

## Annotations

- **label**: Regulation D
- **definition**: securities regulation defining an exemption through which corporations do not have to register their securities and usually do not have to file reports with the SEC
- **adaptedFrom**: Regulation D is defined in the US Code of Federal Regulations (CFR) Title 17, Chapter II, Part 230, clauses 501-508. See https://www.ecfr.gov/current/title-17/chapter-II/part-230?toc=1 for the actual text of the regulation.
- **explanatoryNote**: Issuers must file what's known as a 'Form D' after they first sell their securities if they qualify for registration under Regulation D.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
