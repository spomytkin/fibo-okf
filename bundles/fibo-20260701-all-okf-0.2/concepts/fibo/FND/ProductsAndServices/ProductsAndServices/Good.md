---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: good
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: physical, produced item over which ownership rights can be established, whose ownership can be passed from one
      party to another by engaging in transactions, and that is not money or real estate
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://data.oecd.org/trade/trade-in-goods.htm
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.law.cornell.edu/ucc/9/9-102#goods
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An inherently useful and relatively scarce tangible item produced from agricultural, construction, manufacturing,
      or mining activities. Off-the-shelf products, including off-the-shelf software products and customization of software
      products, are generally considered to be goods. Energy, such as electricity, is also considered to be a good from a
      legal perspective, and meets the criteria of being manufactured or produced via some process, including but not limited
      to a mining process. According to the UN Convention On Contract For The International Sale Of Goods, the term 'good'
      does not include (1) items bought for personal use, (2) items bought at an auction or foreclosure sale, (3) aircraft
      or ocean-going vessels.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: From the Universal Commercial Code (UCC) in the United States, the term 'good' includes (i) fixtures, (ii) standing
      timber that is to be cut and removed under a conveyance or contract for sale, (iii) the unborn young of animals, (iv)
      crops grown, growing, or to be grown, even if the crops are produced on trees, vines, or bushes, and (v) manufactured
      homes. The term also includes a computer program embedded in goods and any supporting information provided in connection
      with a transaction relating to the program if (i) the program is associated with the goods in such a manner that it
      customarily is considered part of the goods, or (ii) by becoming the owner of the goods, a person acquires a right to
      use the program in connection with the goods. The term does not include a computer program embedded in goods that consist
      solely of the medium in which the program is embedded. The term also does not include accounts, chattel paper, commercial
      tort claims, deposit accounts, documents, general intangibles, instruments, investment property, letter-of-credit rights,
      letters of credit, money, or oil, gas, or other minerals before extraction.
  disjoint_with:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/AmountOfMoney.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/AmountOfMoney
  - concept: /concepts/fibo/FND/Places/RealProperty/RealEstate.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealEstate
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Good
sources:
- id: fibo-source-7f330c2b6d
  resource: references/fibo/FND/ProductsAndServices/ProductsAndServices.rdf
  sha256: 7f330c2b6de4e90f2c5d728ddf32af1d75f320646040450c1da9a8c5f8740548
  title: FIBO source FND/ProductsAndServices/ProductsAndServices.rdf
title: good
type: Ontology Class
---

# good

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Good>

## Definition

physical, produced item over which ownership rights can be established, whose ownership can be passed from one party to another by engaging in transactions, and that is not money or real estate

## Constraints

- **Disjoint with**: [AmountOfMoney](/concepts/fibo/FND/Accounting/CurrencyAmount/AmountOfMoney.md)
- **Disjoint with**: [RealEstate](/concepts/fibo/FND/Places/RealProperty/RealEstate.md)

## Annotations

- **label**: good
- **definition**: physical, produced item over which ownership rights can be established, whose ownership can be passed from one party to another by engaging in transactions, and that is not money or real estate
- **adaptedFrom**: https://data.oecd.org/trade/trade-in-goods.htm
- **adaptedFrom**: https://www.law.cornell.edu/ucc/9/9-102#goods
- **explanatoryNote**: An inherently useful and relatively scarce tangible item produced from agricultural, construction, manufacturing, or mining activities. Off-the-shelf products, including off-the-shelf software products and customization of software products, are generally considered to be goods. Energy, such as electricity, is also considered to be a good from a legal perspective, and meets the criteria of being manufactured or produced via some process, including but not limited to a mining process. According to the UN Convention On Contract For The International Sale Of Goods, the term 'good' does not include (1) items bought for personal use, (2) items bought at an auction or foreclosure sale, (3) aircraft or ocean-going vessels.
- **explanatoryNote**: From the Universal Commercial Code (UCC) in the United States, the term 'good' includes (i) fixtures, (ii) standing timber that is to be cut and removed under a conveyance or contract for sale, (iii) the unborn young of animals, (iv) crops grown, growing, or to be grown, even if the crops are produced on trees, vines, or bushes, and (v) manufactured homes. The term also includes a computer program embedded in goods and any supporting information provided in connection with a transaction relating to the program if (i) the program is associated with the goods in such a manner that it customarily is considered part of the goods, or (ii) by becoming the owner of the goods, a person acquires a right to use the program in connection with the goods. The term does not include a computer program embedded in goods that consist solely of the medium in which the program is embedded. The term also does not include accounts, chattel paper, commercial tort claims, deposit accounts, documents, general intangibles, instruments, investment property, letter-of-credit rights, letters of credit, money, or oil, gas, or other minerals before extraction.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
