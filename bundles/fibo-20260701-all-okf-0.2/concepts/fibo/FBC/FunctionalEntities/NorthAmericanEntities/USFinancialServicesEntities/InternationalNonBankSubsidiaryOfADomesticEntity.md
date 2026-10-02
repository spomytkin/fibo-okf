---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: international non-bank subsidiary of a domestic entity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: non-bank financial service provider based outside of the United States of which 25 percent or more of whose voting
      shares are owned or controlled by an entity that is based in the United States, or of which a majority of its directors
      are controlled by such domestic entity, or of which 25 percent or more of whose voting shares are held by trustees for
      the benefit of the shareholders or members of such domestic entity
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ffiec.gov/npw/Help/InstitutionTypes
  disjoint_with:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/DomesticNonBankSubsidiaryOfADomesticEntity.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/DomesticNonBankSubsidiaryOfADomesticEntity
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-INB
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://fraser.stlouisfed.org/title/bank-holding-company-act-1956-984/fulltext
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/NonBankSubsidiaryOfADomesticEntity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/NonBankSubsidiaryOfADomesticEntity
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/InternationalNonBankSubsidiaryOfADomesticEntity
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
- id: fibo-source-ec9acb8223
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
  sha256: ec9acb82235dfc421e0f84c8e1eeab8d4593b678b5339868d9cf247161f7283c
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
title: international non-bank subsidiary of a domestic entity
type: Ontology Class
---

# international non-bank subsidiary of a domestic entity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/InternationalNonBankSubsidiaryOfADomesticEntity>

## Definition

non-bank financial service provider based outside of the United States of which 25 percent or more of whose voting shares are owned or controlled by an entity that is based in the United States, or of which a majority of its directors are controlled by such domestic entity, or of which 25 percent or more of whose voting shares are held by trustees for the benefit of the shareholders or members of such domestic entity

## Relationships

- **See also**: [fulltext](<https://fraser.stlouisfed.org/title/bank-holding-company-act-1956-984/fulltext>)
- **Subclass of**: [NonBankSubsidiaryOfADomesticEntity](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/NonBankSubsidiaryOfADomesticEntity.md)

## Constraints

- **Disjoint with**: [DomesticNonBankSubsidiaryOfADomesticEntity](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/DomesticNonBankSubsidiaryOfADomesticEntity.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-INB`

## Annotations

- **label**: international non-bank subsidiary of a domestic entity
- **definition**: non-bank financial service provider based outside of the United States of which 25 percent or more of whose voting shares are owned or controlled by an entity that is based in the United States, or of which a majority of its directors are controlled by such domestic entity, or of which 25 percent or more of whose voting shares are held by trustees for the benefit of the shareholders or members of such domestic entity
- **adaptedFrom**: https://www.ffiec.gov/npw/Help/InstitutionTypes

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
