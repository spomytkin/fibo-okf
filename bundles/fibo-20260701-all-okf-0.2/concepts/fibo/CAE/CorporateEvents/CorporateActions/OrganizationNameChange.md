---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: organization name change
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: information action that provides details of name changes for a legal entity
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#note
    value: Name changes may include legal name changes as well as 'doing business as', and other operational names for an
      organization.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/Notification.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/Notification
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/OrganizationNameChange
sources:
- id: fibo-source-54455443d7
  resource: references/fibo/CAE/CorporateEvents/CorporateActions.rdf
  sha256: 54455443d756001807a44fb86449f950a37301ed0646079052aa300d4b315193
  title: FIBO source CAE/CorporateEvents/CorporateActions.rdf
title: organization name change
type: Ontology Class
---

# organization name change

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/OrganizationNameChange>

## Definition

information action that provides details of name changes for a legal entity

## Relationships

- **Subclass of**: [Notification](/concepts/fibo/CAE/CorporateEvents/CorporateActions/Notification.md)

## Annotations

- **label** (en): organization name change
- **definition** (en): information action that provides details of name changes for a legal entity
- **note** (en): Name changes may include legal name changes as well as 'doing business as', and other operational names for an organization.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
