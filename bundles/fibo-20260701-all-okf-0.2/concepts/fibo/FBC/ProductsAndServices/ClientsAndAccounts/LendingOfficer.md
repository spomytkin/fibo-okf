---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: lending officer
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporate officer that has overarching responsibility for the relationship with a specific borrower or account
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/CorporateOfficer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/CorporateOfficer
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/RelationshipManager.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/RelationshipManager
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LendingOfficer
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: lending officer
type: Ontology Class
---

# lending officer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LendingOfficer>

## Definition

corporate officer that has overarching responsibility for the relationship with a specific borrower or account

## Relationships

- **Subclass of**: [CorporateOfficer](/concepts/fibo/BE/OwnershipAndControl/Executives/CorporateOfficer.md)
- **Subclass of**: [RelationshipManager](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/RelationshipManager.md)

## Annotations

- **label**: lending officer
- **definition**: corporate officer that has overarching responsibility for the relationship with a specific borrower or account

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
