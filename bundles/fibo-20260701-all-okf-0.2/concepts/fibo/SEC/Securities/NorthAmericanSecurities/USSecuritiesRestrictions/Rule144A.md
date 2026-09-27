---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Rule 144A
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: securities regulation that allows investors to resell privately placed securities to qualified institutional buyers
      (QIBs) under certain conditions
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Rule 144A is defined in the US Code of Federal Regulations (CFR) Title 17, Chapter II, Part 230, clause 144A -
      Private resales of securities to institutions. See https://www.ecfr.gov/current/title-17/chapter-II/part-230?toc=1 for
      the actual text of the regulation.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: QIBs are institutional investors with at least $100 million invested in securities. Rule 144A provides an exemption
      from SEC registration for these resales.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Rule 144 section A is a Securities & Exchange Commission rule that establishes specific criteria for determining
      whether a person is not engaged in a distribution and creates a safe harbor from the Section 2(a)(11) definition of
      'underwriter'. It modifies holding period requirements on privately placed securities to permit qualified institutional
      buyers to trade these positions among themselves.
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/LegalHoldingRestriction
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction.md
    predicate: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.sec.gov/divisions/corpfin/ecfrlinks
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/Rule144A
sources:
- id: fibo-source-91c51c4810
  resource: references/fibo/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions.rdf
  sha256: 91c51c4810cfe6c5acc0aaf99de529357298d47f01cfe4f5eee4962f40f5be33
  title: FIBO source SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions.rdf
title: Rule 144A
type: Ontology Individual
---

# Rule 144A

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/Rule144A>

## Definition

securities regulation that allows investors to resell privately placed securities to qualified institutional buyers (QIBs) under certain conditions

## Relationships

- **Related to**: [UnitedStatesJurisdiction](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction.md)
- **See also**: [ecfrlinks](<https://www.sec.gov/divisions/corpfin/ecfrlinks>)

## Annotations

- **label**: Rule 144A
- **definition**: securities regulation that allows investors to resell privately placed securities to qualified institutional buyers (QIBs) under certain conditions
- **adaptedFrom**: Rule 144A is defined in the US Code of Federal Regulations (CFR) Title 17, Chapter II, Part 230, clause 144A - Private resales of securities to institutions. See https://www.ecfr.gov/current/title-17/chapter-II/part-230?toc=1 for the actual text of the regulation.
- **explanatoryNote**: QIBs are institutional investors with at least $100 million invested in securities. Rule 144A provides an exemption from SEC registration for these resales.
- **explanatoryNote**: Rule 144 section A is a Securities & Exchange Commission rule that establishes specific criteria for determining whether a person is not engaged in a distribution and creates a safe harbor from the Section 2(a)(11) definition of 'underwriter'. It modifies holding period requirements on privately placed securities to permit qualified institutional buyers to trade these positions among themselves.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
