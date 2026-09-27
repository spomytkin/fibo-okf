---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: agency of a foreign banking organization
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: place of business of a foreign bank, located in any state, at which credit balances are maintained, checks are
      paid, money is lent, or, to the extent not prohibited by state or federal law, deposits are accepted from a person or
      entity that is not a citizen or resident of the United States
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-211/subpart-B/section-211.21
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ffiec.gov/npw/Help/InstitutionTypes
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.govinfo.gov/content/pkg/COMPS-275/pdf/COMPS-275.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: "Obligations shall not be considered credit balances unless they are: \n(1) Incidental to, or arise out of the\
      \ exercise of, other lawful banking powers; \n(2) To serve a specific purpose; \n(3) Not solicited from the general\
      \ public; \n(4) Not used to pay routine operating expenses in the United States such as salaries, rent, or taxes; \n\
      (5) Withdrawn within a reasonable period of time after the specific purpose for which they were placed has been accomplished;\
      \ and \n(6) Drawn upon in a manner reasonable in relation to the size and nature of the account."
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ForeignBank
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isControlledPartyOf
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ForeignBank
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/isOwnedAsset
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: Nb8161f35577a42468fc2432d29d81c82
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/OfficeOfAForeignBank
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/AgencyOfAForeignBankingOrganization
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
title: agency of a foreign banking organization
type: Ontology Class
---

# agency of a foreign banking organization

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/AgencyOfAForeignBankingOrganization>

## Definition

place of business of a foreign bank, located in any state, at which credit balances are maintained, checks are paid, money is lent, or, to the extent not prohibited by state or federal law, deposits are accepted from a person or entity that is not a citizen or resident of the United States

## Relationships

- **Subclass of**: [FinancialInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)

## Constraints

- **[isControlledPartyOf](/concepts/fibo/FND/OwnershipAndControl/Control/isControlledPartyOf.md)**: some values from of type [ForeignBank](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ForeignBank.md)
- **[isOwnedAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/isOwnedAsset.md)**: some values from of type [ForeignBank](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ForeignBank.md)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `Nb8161f35577a42468fc2432d29d81c82`
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from of type [OfficeOfAForeignBank](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/OfficeOfAForeignBank.md)

## Annotations

- **label**: agency of a foreign banking organization
- **definition**: place of business of a foreign bank, located in any state, at which credit balances are maintained, checks are paid, money is lent, or, to the extent not prohibited by state or federal law, deposits are accepted from a person or entity that is not a citizen or resident of the United States
- **adaptedFrom**: https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-211/subpart-B/section-211.21
- **adaptedFrom**: https://www.ffiec.gov/npw/Help/InstitutionTypes
- **adaptedFrom**: https://www.govinfo.gov/content/pkg/COMPS-275/pdf/COMPS-275.pdf
- **explanatoryNote**: Obligations shall not be considered credit balances unless they are:  (1) Incidental to, or arise out of the exercise of, other lawful banking powers;  (2) To serve a specific purpose;  (3) Not solicited from the general public;  (4) Not used to pay routine operating expenses in the United States such as salaries, rent, or taxes;  (5) Withdrawn within a reasonable period of time after the specific purpose for which they were placed has been accomplished; and  (6) Drawn upon in a manner reasonable in relation to the size and nature of the account.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
