---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: foreign bank
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial institution organized under the laws of a foreign country, a territory of the United States, Puerto Rico,
      Guam, American Samoa, or the Virgin Islands, which engages in the business of banking, or any subsidiary or affiliate,
      organized under such laws, of any such institution
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-211/subpart-B/section-211.21
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ffiec.gov/nicpubweb/Content/HELP/Institution%20Type%20Description.htm
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.govinfo.gov/content/pkg/COMPS-275/pdf/COMPS-275.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: For the purposes of the International Banking Act of 1978, the term 'foreign bank' includes, without limitation,
      foreign commercial banks, foreign merchant banks and other foreign institutions that engage in banking activities usual
      in connection with the business of banking in the countries where such foreign institutions are organized or operating.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Foreign bank means an organization that is organized under the laws of a foreign country and that engages directly
      in the business of banking outside the United States. The term foreign bank does not include a central bank of a foreign
      country that does not engage or seek to engage in a commercial banking business in the United States through an office.
  disjoint_with:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/CentralBank.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/CentralBank
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/USBank.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/USBank
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
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-FBK
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/Bank.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/Bank
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ForeignBank
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
- id: fibo-source-ec9acb8223
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
  sha256: ec9acb82235dfc421e0f84c8e1eeab8d4593b678b5339868d9cf247161f7283c
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
title: foreign bank
type: Ontology Class
---

# foreign bank

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/ForeignBank>

## Definition

financial institution organized under the laws of a foreign country, a territory of the United States, Puerto Rico, Guam, American Samoa, or the Virgin Islands, which engages in the business of banking, or any subsidiary or affiliate, organized under such laws, of any such institution

## Relationships

- **Subclass of**: [Bank](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/Bank.md)

## Constraints

- **Disjoint with**: [CentralBank](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/CentralBank.md)
- **Disjoint with**: [USBank](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/USBank.md)
- **[hasHomeCountry](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/hasHomeCountry.md)**: some values from of type [Country](<https://www.omg.org/spec/Commons/Locations/Country>)
- **[hasHomeCountrySupervisor](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/hasHomeCountrySupervisor.md)**: min qualified cardinality 0 of type [RegulatoryAgency](<https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency>)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-FBK`

## Annotations

- **label**: foreign bank
- **definition**: financial institution organized under the laws of a foreign country, a territory of the United States, Puerto Rico, Guam, American Samoa, or the Virgin Islands, which engages in the business of banking, or any subsidiary or affiliate, organized under such laws, of any such institution
- **adaptedFrom**: https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-211/subpart-B/section-211.21
- **adaptedFrom**: https://www.ffiec.gov/nicpubweb/Content/HELP/Institution%20Type%20Description.htm
- **adaptedFrom**: https://www.govinfo.gov/content/pkg/COMPS-275/pdf/COMPS-275.pdf
- **explanatoryNote**: For the purposes of the International Banking Act of 1978, the term 'foreign bank' includes, without limitation, foreign commercial banks, foreign merchant banks and other foreign institutions that engage in banking activities usual in connection with the business of banking in the countries where such foreign institutions are organized or operating.
- **explanatoryNote**: Foreign bank means an organization that is organized under the laws of a foreign country and that engages directly in the business of banking outside the United States. The term foreign bank does not include a central bank of a foreign country that does not engage or seek to engage in a commercial banking business in the United States through an office.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
