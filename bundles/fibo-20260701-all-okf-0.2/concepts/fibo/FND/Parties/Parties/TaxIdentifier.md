---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: tax identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifier assigned to a taxpayer that enables compulsory financial charges and other levies to be imposed on the
      taxpayer by a governmental organization in order to fund government spending and various public expenditures
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.oecd-ilibrary.org/taxation/standard-for-automatic-exchange-of-financial-account-information-in-tax-matters-second-edition_9789264267992-en
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Tax identifiers are used for various tax-related purposes in the United States and in other countries under the
      Common Reporting Standard (CRS).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/TaxIdentificationScheme
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/isMemberOf
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/Identifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/TaxIdentifier
sources:
- id: fibo-source-9758af6c79
  resource: references/fibo/BE/LegalEntities/FormalBusinessOrganizations.rdf
  sha256: 9758af6c796f157eedb21d72cde0822cb7a2ecbd6b5a70ef23be48121c598ede
  title: FIBO source BE/LegalEntities/FormalBusinessOrganizations.rdf
- id: fibo-source-2c7ef9cc41
  resource: references/fibo/FND/Parties/Parties.rdf
  sha256: 2c7ef9cc4107e85b5bba3894094e496bcf4e8fe3ef9d6ce3b7d0830fb284f61d
  title: FIBO source FND/Parties/Parties.rdf
title: tax identifier
type: Ontology Class
---

# tax identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/TaxIdentifier>

## Definition

identifier assigned to a taxpayer that enables compulsory financial charges and other levies to be imposed on the taxpayer by a governmental organization in order to fund government spending and various public expenditures

## Relationships

- **Subclass of**: [Identifier](<https://www.omg.org/spec/Commons/Identifiers/Identifier>)

## Constraints

- **[isMemberOf](<https://www.omg.org/spec/Commons/Collections/isMemberOf>)**: exact qualified cardinality 1 of type [TaxIdentificationScheme](/concepts/fibo/FND/Parties/Parties/TaxIdentificationScheme.md)
- **[isApplicableIn](<https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn>)**: some values from of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)
- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)

## Annotations

- **label**: tax identifier
- **definition**: identifier assigned to a taxpayer that enables compulsory financial charges and other levies to be imposed on the taxpayer by a governmental organization in order to fund government spending and various public expenditures
- **adaptedFrom**: https://www.oecd-ilibrary.org/taxation/standard-for-automatic-exchange-of-financial-account-information-in-tax-matters-second-edition_9789264267992-en
- **explanatoryNote**: Tax identifiers are used for various tax-related purposes in the United States and in other countries under the Common Reporting Standard (CRS).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
