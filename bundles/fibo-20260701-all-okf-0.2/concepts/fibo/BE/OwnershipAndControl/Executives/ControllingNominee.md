---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: controlling nominee
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that holds legal title to an asset (e.g., stocks, bonds, or property) on behalf of the beneficial owner
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The nominee is typically the registered owner of an asset, named in official records.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/BusinessAuthorizations/hasDelegatedControlOf
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/BusinessAuthorizations/LegallyDelegatedAuthority
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/ControllingNominee
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: controlling nominee
type: Ontology Class
---

# controlling nominee

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/ControllingNominee>

## Definition

party that holds legal title to an asset (e.g., stocks, bonds, or property) on behalf of the beneficial owner

## Relationships

- **Subclass of**: [LegallyDelegatedAuthority](<https://www.omg.org/spec/Commons/BusinessAuthorizations/LegallyDelegatedAuthority>)

## Constraints

- **[hasDelegatedControlOf](<https://www.omg.org/spec/Commons/BusinessAuthorizations/hasDelegatedControlOf>)**: some values from of type [Asset](/concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md)

## Annotations

- **label** (en): controlling nominee
- **definition**: party that holds legal title to an asset (e.g., stocks, bonds, or property) on behalf of the beneficial owner
- **explanatoryNote**: The nominee is typically the registered owner of an asset, named in official records.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
