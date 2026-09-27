---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: value-added tax identification number
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: tax identifier that identifies a taxable person (business) or non-taxable legal entity for a consumption tax that
      is assessed incrementally, levied on the price of a product or service at each stage of production, distribution, and
      sale to the end consumer
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: VATIN
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://ec.europa.eu/taxation_customs/business/vat/eu-vat-rules-topic/vat-identification-numbers_en
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: If the ultimate consumer is a business that collects and pays to the government VAT on its products or services,
      it can reclaim the tax paid. Not all localities require VAT to be charged, and exports are often exempt. VAT is usually
      implemented as a destination-based tax, where the tax rate is based on the location of the consumer and applied to the
      sales price.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: VAT identification number
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: VAT registration number
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Parties/Parties/TaxIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/TaxIdentifier
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/OrganizationIdentifier
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegisteredIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/ValueAddedTaxIdentificationNumber
sources:
- id: fibo-source-9758af6c79
  resource: references/fibo/BE/LegalEntities/FormalBusinessOrganizations.rdf
  sha256: 9758af6c796f157eedb21d72cde0822cb7a2ecbd6b5a70ef23be48121c598ede
  title: FIBO source BE/LegalEntities/FormalBusinessOrganizations.rdf
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: value-added tax identification number
type: Ontology Class
---

# value-added tax identification number

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/ValueAddedTaxIdentificationNumber>

## Definition

tax identifier that identifies a taxable person (business) or non-taxable legal entity for a consumption tax that is assessed incrementally, levied on the price of a product or service at each stage of production, distribution, and sale to the end consumer

## Relationships

- **Subclass of**: [TaxIdentifier](/concepts/fibo/FND/Parties/Parties/TaxIdentifier.md)
- **Subclass of**: [OrganizationIdentifier](<https://www.omg.org/spec/Commons/Organizations/OrganizationIdentifier>)
- **Subclass of**: [RegisteredIdentifier](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegisteredIdentifier>)

## Annotations

- **label**: value-added tax identification number
- **definition**: tax identifier that identifies a taxable person (business) or non-taxable legal entity for a consumption tax that is assessed incrementally, levied on the price of a product or service at each stage of production, distribution, and sale to the end consumer
- **abbreviation**: VATIN
- **adaptedFrom**: https://ec.europa.eu/taxation_customs/business/vat/eu-vat-rules-topic/vat-identification-numbers_en
- **explanatoryNote**: If the ultimate consumer is a business that collects and pays to the government VAT on its products or services, it can reclaim the tax paid. Not all localities require VAT to be charged, and exports are often exempt. VAT is usually implemented as a destination-based tax, where the tax rate is based on the location of the consumer and applied to the sales price.
- **synonym**: VAT identification number
- **synonym**: VAT registration number

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
