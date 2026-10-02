---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: beneficial owner
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that enjoys the benefits of ownership (such as receipt of income) of something even though its ownership
      (title) may be in the name of another party (called a nominee or registered owner)
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://en.wikipedia.org/wiki/Beneficial_ownership#Financial_Action_Task_Force_on_Money_Laundering_(FATF)
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.fincen.gov/resources/statutes-regulations/guidance/guidance-obtaining-and-retaining-beneficial-ownership
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ncua.gov/regulation-supervision/letters-credit-unions-other-guidance/beneficial-ownership-requirements-legal-entity-customers-overview
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'From World Bank Report: In identifying the beneficial owner, the focus should be on two factors: the control exercised
      and the benefit derived. Control of a corporate vehicle will always depend on context, as control can be exercised in
      many different ways, including through ownership, contractually or informally.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The Financial Action Task Force on Money Laundering (FATF) refers to a 'beneficial owner' as the natural person(s)
      who ultimately owns or controls a legal entity and/or the natural person on whose behalf a transaction is being conducted.
      It also includes those persons who exercise ultimate effective control over a legal person or arrangement.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The National Credit Union Administration (NCUA) defines a 'beneficial owner' as (1) a single individual with significant
      responsibility to control, manage or direct a legal entity customer, or (2) each individual, if any, who, directly or
      indirectly, through any contract, arrangement, understanding, relationship or otherwise, owns 25 percent or more of
      the equity interests of a legal entity customer; if a trust owns directly or indirectly, through any contract, arrangement,
      understanding, relationship or otherwise, 25 percent or more of the equity interests of a legal entity customer, the
      beneficial owner is the trustee.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Use of a nominee (who may be an agent, custodian, or a trustee) does not change the position regarding tax reporting
      and tax liability, and the beneficial owner remains responsible.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/isBeneficialOwnerOf
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/ControllingNominee
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/BusinessAuthorizations/delegatesControlTo
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Owner.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Owner
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwner
sources:
- id: fibo-source-4d1bc90c45
  resource: references/fibo/BE/OwnershipAndControl/CorporateOwnership.rdf
  sha256: 4d1bc90c4583cdc3c4f8228a8afb505706731dd0d76b848f6678e714ee5ac147
  title: FIBO source BE/OwnershipAndControl/CorporateOwnership.rdf
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: beneficial owner
type: Ontology Class
---

# beneficial owner

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwner>

## Definition

party that enjoys the benefits of ownership (such as receipt of income) of something even though its ownership (title) may be in the name of another party (called a nominee or registered owner)

## Relationships

- **Subclass of**: [Owner](/concepts/fibo/FND/OwnershipAndControl/Ownership/Owner.md)

## Constraints

- **[isBeneficialOwnerOf](/concepts/fibo/BE/OwnershipAndControl/CorporateOwnership/isBeneficialOwnerOf.md)**: some values from of type [Asset](/concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md)
- **[delegatesControlTo](<https://www.omg.org/spec/Commons/BusinessAuthorizations/delegatesControlTo>)**: some values from of type [ControllingNominee](/concepts/fibo/BE/OwnershipAndControl/Executives/ControllingNominee.md)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: exact qualified cardinality 1 of type [LegallyCompetentNaturalPerson](/concepts/fibo/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md)

## Annotations

- **label**: beneficial owner
- **definition**: party that enjoys the benefits of ownership (such as receipt of income) of something even though its ownership (title) may be in the name of another party (called a nominee or registered owner)
- **adaptedFrom**: https://en.wikipedia.org/wiki/Beneficial_ownership#Financial_Action_Task_Force_on_Money_Laundering_(FATF)
- **adaptedFrom**: https://www.fincen.gov/resources/statutes-regulations/guidance/guidance-obtaining-and-retaining-beneficial-ownership
- **adaptedFrom**: https://www.ncua.gov/regulation-supervision/letters-credit-unions-other-guidance/beneficial-ownership-requirements-legal-entity-customers-overview
- **explanatoryNote**: From World Bank Report: In identifying the beneficial owner, the focus should be on two factors: the control exercised and the benefit derived. Control of a corporate vehicle will always depend on context, as control can be exercised in many different ways, including through ownership, contractually or informally.
- **explanatoryNote**: The Financial Action Task Force on Money Laundering (FATF) refers to a 'beneficial owner' as the natural person(s) who ultimately owns or controls a legal entity and/or the natural person on whose behalf a transaction is being conducted. It also includes those persons who exercise ultimate effective control over a legal person or arrangement.
- **explanatoryNote**: The National Credit Union Administration (NCUA) defines a 'beneficial owner' as (1) a single individual with significant responsibility to control, manage or direct a legal entity customer, or (2) each individual, if any, who, directly or indirectly, through any contract, arrangement, understanding, relationship or otherwise, owns 25 percent or more of the equity interests of a legal entity customer; if a trust owns directly or indirectly, through any contract, arrangement, understanding, relationship or otherwise, 25 percent or more of the equity interests of a legal entity customer, the beneficial owner is the trustee.
- **explanatoryNote**: Use of a nominee (who may be an agent, custodian, or a trustee) does not change the position regarding tax reporting and tax liability, and the beneficial owner remains responsible.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
