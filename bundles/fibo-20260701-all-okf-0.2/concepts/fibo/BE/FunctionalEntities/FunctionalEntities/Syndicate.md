---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: syndicate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: temporary, self-organizing group of people, companies, corporations or entities organized as an alliance whose
      purpose is to transact some specific business, or to pursue or promote a shared interest
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: For example, when a group of investment banks work together to bring a new issue of securities to the market, they
      form a distributing syndicate. Other types of syndicates are created for underwriting, banking, and insurance.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A syndicate is a temporary alliance formed by people or businesses to handle a large transaction that would be
      hard to execute individually. Syndication makes it easy for businesses to pool their resources and share risks.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/Organization
resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/Syndicate
sources:
- id: fibo-source-1a60609b6a
  resource: references/fibo/BE/FunctionalEntities/FunctionalEntities.rdf
  sha256: 1a60609b6ad170e85bb9424d06c7d8f740d0c98492e22a8c0c9e2e285ec47b5a
  title: FIBO source BE/FunctionalEntities/FunctionalEntities.rdf
title: syndicate
type: Ontology Class
---

# syndicate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/Syndicate>

## Definition

temporary, self-organizing group of people, companies, corporations or entities organized as an alliance whose purpose is to transact some specific business, or to pursue or promote a shared interest

## Relationships

- **Subclass of**: [Organization](<https://www.omg.org/spec/Commons/Organizations/Organization>)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)

## Annotations

- **label** (en): syndicate
- **definition** (en): temporary, self-organizing group of people, companies, corporations or entities organized as an alliance whose purpose is to transact some specific business, or to pursue or promote a shared interest
- **example** (en): For example, when a group of investment banks work together to bring a new issue of securities to the market, they form a distributing syndicate. Other types of syndicates are created for underwriting, banking, and insurance.
- **explanatoryNote** (en): A syndicate is a temporary alliance formed by people or businesses to handle a large transaction that would be hard to execute individually. Syndication makes it easy for businesses to pool their resources and share risks.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
