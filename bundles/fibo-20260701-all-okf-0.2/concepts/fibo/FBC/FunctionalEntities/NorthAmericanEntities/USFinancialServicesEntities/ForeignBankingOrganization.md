---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: foreign banking organization
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial service provider that is headquartered outside the United States and that can acquire or establish freestanding
      banks or bank holding companies in the United States
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: FBO
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-211/subpart-B/section-211.21
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ffiec.gov/nicpubweb/Content/HELP/Institution%20Type%20Description.htm
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: "Foreign banking organization means: \n(1) A foreign bank, as defined in section 1(b)(7) of the International Banking\
      \ Act of 1978 (12 U.S.C. 3101(7)), that: \n\t(i) Operates a branch, agency, or commercial lending company subsidiary\
      \ in the United States; \n\t(ii) Controls a bank in the United States; or \n\t(iii) Controls an Edge corporation acquired\
      \ after March 5, 1987; and \n(2) Any company of which the foreign bank is a subsidiary."
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: These entities are regulated and supervised as domestic institutions.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/Locations/Country
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/hasHomeCountry
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/hasHomeCountrySupervisor
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-FBO
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ForeignBankingOrganization
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
- id: fibo-source-ec9acb8223
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
  sha256: ec9acb82235dfc421e0f84c8e1eeab8d4593b678b5339868d9cf247161f7283c
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
title: foreign banking organization
type: Ontology Class
---

# foreign banking organization

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ForeignBankingOrganization>

## Definition

financial service provider that is headquartered outside the United States and that can acquire or establish freestanding banks or bank holding companies in the United States

## Relationships

- **Subclass of**: [FinancialServiceProvider](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)

## Constraints

- **[hasHomeCountry](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/hasHomeCountry.md)**: some values from of type [Country](<https://www.omg.org/spec/Commons/Locations/Country>)
- **[hasHomeCountrySupervisor](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/hasHomeCountrySupervisor.md)**: min qualified cardinality 0 of type [RegulatoryAgency](<https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency>)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-FBO`

## Annotations

- **label**: foreign banking organization
- **definition**: financial service provider that is headquartered outside the United States and that can acquire or establish freestanding banks or bank holding companies in the United States
- **abbreviation**: FBO
- **adaptedFrom**: https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-211/subpart-B/section-211.21
- **adaptedFrom**: https://www.ffiec.gov/nicpubweb/Content/HELP/Institution%20Type%20Description.htm
- **explanatoryNote**: Foreign banking organization means:  (1) A foreign bank, as defined in section 1(b)(7) of the International Banking Act of 1978 (12 U.S.C. 3101(7)), that:  	(i) Operates a branch, agency, or commercial lending company subsidiary in the United States;  	(ii) Controls a bank in the United States; or  	(iii) Controls an Edge corporation acquired after March 5, 1987; and  (2) Any company of which the foreign bank is a subsidiary.
- **explanatoryNote**: These entities are regulated and supervised as domestic institutions.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
