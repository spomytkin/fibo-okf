---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: financial holding company
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial entity engaged in a broad range of banking-related activities as permitted under the Gramm-Leach-Bliley
      Act of 1999
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: Can be a domestic or foreign domiciled holding company
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ffiec.gov/npw/Help/InstitutionTypes
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'These activities include: insurance underwriting, securities dealing and underwriting, financial and investment
      advisory services, merchant banking, issuing or selling securitized interests in bank-eligible assets, and generally
      engaging in any non-banking activity authorized by the Bank Holding Company Act. The Federal Reserve Board is responsible
      for supervising the financial condition and activities of financial holding companies. Similarly, any non-bank commercial
      company that is predominantly engaged in financial activities, earning 85 percent or more of its gross revenues from
      financial services, may choose to become a financial holding company. These companies are required to sell any non-financial
      (commercial) businesses within ten years.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: Financial Holding Company / BHC
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/hasPrimaryFederalRegulator
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/BoardOfGovernorsOfTheFederalReserveSystem
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-FHD
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/BankHoldingCompany.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BankHoldingCompany
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/FinancialHoldingCompany
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
- id: fibo-source-ec9acb8223
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
  sha256: ec9acb82235dfc421e0f84c8e1eeab8d4593b678b5339868d9cf247161f7283c
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies.rdf
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: financial holding company
type: Ontology Class
---

# financial holding company

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/FinancialHoldingCompany>

## Definition

financial entity engaged in a broad range of banking-related activities as permitted under the Gramm-Leach-Bliley Act of 1999

## Relationships

- **Subclass of**: [BankHoldingCompany](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/BankHoldingCompany.md)

## Constraints

- **[hasPrimaryFederalRegulator](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/hasPrimaryFederalRegulator.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/BoardOfGovernorsOfTheFederalReserveSystem`
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-FHD`

## Annotations

- **label**: financial holding company
- **definition**: financial entity engaged in a broad range of banking-related activities as permitted under the Gramm-Leach-Bliley Act of 1999
- **note**: Can be a domestic or foreign domiciled holding company
- **adaptedFrom**: https://www.ffiec.gov/npw/Help/InstitutionTypes
- **explanatoryNote**: These activities include: insurance underwriting, securities dealing and underwriting, financial and investment advisory services, merchant banking, issuing or selling securitized interests in bank-eligible assets, and generally engaging in any non-banking activity authorized by the Bank Holding Company Act. The Federal Reserve Board is responsible for supervising the financial condition and activities of financial holding companies. Similarly, any non-bank commercial company that is predominantly engaged in financial activities, earning 85 percent or more of its gross revenues from financial services, may choose to become a financial holding company. These companies are required to sell any non-financial (commercial) businesses within ten years.
- **synonym**: Financial Holding Company / BHC

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
